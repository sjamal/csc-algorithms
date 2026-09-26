# Runbook: Running and Testing

How to set up, test, and run `csc-algorithms` locally. For the contribution and PR workflow, see [Contributing](CONTRIBUTING.md).

## 1. Setup

Requires Python 3.10+.

**With uv (recommended):**
```bash
git clone https://github.com/sjamal/csc-algorithms.git
cd csc-algorithms
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e '.[dev]'
source .venv/bin/activate
```

**With pip:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'        # or: pip install -r requirements.txt
```

Install the pre-commit hook once per clone:
```bash
git config core.hooksPath .githooks
```

## 2. Testing

| Goal | Command |
|---|---|
| Full suite | `pytest tests/` |
| One domain | `pytest tests/test_graphs.py -v` |
| One test | `pytest tests/test_graphs.py -k traveling -v` |
| Selected files (Makefile) | `make test-fast TEST_FILES="tests/test_graphs.py tests/test_service_tools.py"` |
| 100% coverage gate | `make test-full` |
| Format check + coverage gate | `make verify` |
| HTML coverage report | `pytest tests/ --cov=src --cov=service --cov-report=html` then open `htmlcov/index.html` |
| Auto-format | `black src/ tests/ service/` |

If the venv is not activated, prefix tools with `.venv/bin/` or pass them to make: `make verify PYTEST=.venv/bin/pytest BLACK=.venv/bin/black`.

CI runs `make test-full` on every push and pull request to `main` and `develop` (see [ci.yml](../.github/workflows/ci.yml)).

## 3. Using the Algorithms from Python
```python
from src.graphs.traveling_salesman import held_karp, nearest_neighbor_two_opt
from src.sorting.merge_sort import merge_sort

merge_sort([5, 2, 4, 1, 3])                     # [1, 2, 3, 4, 5]

edges = [("A", "B", 1), ("B", "C", 1), ("C", "D", 1),
         ("D", "A", 1), ("A", "C", 2), ("B", "D", 2)]
held_karp(["A", "B", "C", "D"], edges)          # (['A', 'D', 'C', 'B', 'A'], 4)
```

See the [algorithm catalog](algorithms.md) for every module and its complexity.

## 4. Running the HTTP API

```bash
uvicorn service.http_app:app --reload
```

Interactive docs: <http://127.0.0.1:8000/docs>

### Sample Requests
```bash
# Sorting
curl -s -X POST http://127.0.0.1:8000/sorting/merge-sort \
  -H 'Content-Type: application/json' -d '{"values": [5, 2, 4, 1, 3]}'

# Shortest paths
curl -s -X POST http://127.0.0.1:8000/graphs/dijkstra \
  -H 'Content-Type: application/json' \
  -d '{"graph": {"A": [["B", 1], ["C", 4]], "B": [["C", 1]], "C": []}, "source": "A"}'

# Traveling Salesman (method: auto | exact | heuristic)
curl -s -X POST http://127.0.0.1:8000/graphs/traveling-salesman \
  -H 'Content-Type: application/json' \
  -d '{"vertices": ["A","B","C","D"],
       "edges": [["A","B",1],["B","C",1],["C","D",1],["D","A",1],["A","C",2],["B","D",2]],
       "method": "auto"}'

# K-Means with an explicit seed
curl -s -X POST http://127.0.0.1:8000/machine-learning/kmeans \
  -H 'Content-Type: application/json' \
  -d '{"points": [[0,0],[0,1],[10,10],[10,11]], "k": 2, "seed": 7}'
```

### Responses
| Status | Meaning |
|---|---|
| 200 | Success; JSON result |
| 400 | Input rejected by the algorithm (e.g., disconnected graph); `detail` explains why |
| 422 | Request failed schema validation or exceeded a request limit |

### Request Limits
The HTTP API caps request sizes to bound CPU and memory per call ([ADR 0000 amendment](adr/0000-expose-algorithms-via-mcp-and-http-service-layer.md#amendment-http-request-size-limits)). Constants live in [http_app.py](../service/http_app.py).

| Constant | Value | Applies to |
|---|---|---|
| `MAX_LIST_ITEMS` | 10,000 | Sorting, search, trees, linked list, trie, union-find |
| `MAX_TEXT_LENGTH` | 100,000 chars | KMP, Huffman, parentheses |
| `MAX_LCS_LENGTH` | 2,000 chars | LCS (quadratic table) |
| `MAX_GRAPH_NODES` | 1,000 | Dijkstra, Bellman-Ford, A*, BFS, DFS, topological sort, Kruskal |
| `MAX_GRAPH_EDGES` | 10,000 | Kruskal |
| `MAX_KNAPSACK_ITEMS` / `MAX_KNAPSACK_CAPACITY` | 1,000 / 10,000 | 0/1 Knapsack |
| `MAX_SIEVE_LIMIT` | 1,000,000 | Sieve of Eratosthenes |
| `MAX_POINTS` / `MAX_KMEANS_ITERS` | 10,000 / 1,000 | K-Means, PCA |
| `MAX_TSP_VERTICES` | 200 | Traveling Salesman (exact solver additionally capped at 12) |

The MCP server does not apply these caps; it runs locally for a single trusted client.

## 5. Running the MCP Server

```bash
python -m service.mcp_server
```

The server speaks MCP over stdio. Register it with your client:

**VS Code** (`.vscode/mcp.json`):
```json
{
  "servers": {
    "csc-algorithms": {
      "type": "stdio",
      "command": "${workspaceFolder}/.venv/bin/python",
      "args": ["-m", "service.mcp_server"],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

**Claude Desktop** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "csc-algorithms": {
      "command": "/absolute/path/to/csc-algorithms/.venv/bin/python",
      "args": ["-m", "service.mcp_server"],
      "cwd": "/absolute/path/to/csc-algorithms"
    }
  }
}
```

Every HTTP endpoint has a matching MCP tool (for example, `graph_traveling_salesman`).

## 6. Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: src` | Run from the repository root, or install with `pip install -e .` |
| Pre-commit hook fails with `ModuleNotFoundError` | The hook uses the `pytest`/`black` on your `PATH`; install dependencies there too (see [Contributing](CONTRIBUTING.md#1-environment-setup)) |
| Coverage gate below 100% | Run `make test-full` and add tests for the lines listed under `Missing` |
| HTTP 422 on a large request | The request exceeded a [request limit](#request-limits) |
| TSP returns `"optimal": false` | More than 12 vertices; the heuristic ran. Use `"method": "exact"` only for small graphs |

---
**Related docs:** [Project README](../README.md) · [Algorithm catalog](algorithms.md) · [ADR index](adr/README.md) · [Contributing](CONTRIBUTING.md) · [Roadmap](../ROADMAP.md)
