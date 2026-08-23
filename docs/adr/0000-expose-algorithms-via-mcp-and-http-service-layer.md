# 0. Expose Algorithm Implementations via an MCP Server and HTTP API

* **Status:** Approved
* **Context:** Every algorithm in this repository was previously only consumable by importing Python modules directly. To make these implementations useful to AI agents, chat assistants, and other programmatic callers, a transport layer was needed that could invoke each algorithm without requiring the caller to understand the internal Python package structure.
* **Decision:** We added a `service/` layer, separate from `src/`, containing:
  * `service/tools.py` — transport-agnostic wrapper functions that translate plain JSON-serializable primitives (dict/list/str/int/float) into the native Python/NumPy types each `src/` algorithm expects, and back. This module contains no algorithmic logic of its own.
  * `service/mcp_server.py` — a stdio-transport MCP server (using the official `mcp` Python SDK's `FastMCP` interface) registering one `@mcp.tool()` per algorithm, for direct consumption by MCP-aware agents and chat clients (e.g. Claude Desktop, VS Code).
  * `service/http_app.py` — a FastAPI application exposing the same operations as REST endpoints, for consumption by any HTTP client or non-MCP programmatic caller.
  * Stateful structures (Binary Search Tree, AVL Tree) are exposed **statelessly**: each call accepts the full list of values to insert and an optional value to search for, returning the resulting tree layout in one round trip. No server-side session state is held between calls.
* **Consequences:**
  * Both transports call the exact same `service/tools.py` functions, guaranteeing identical results and a single source of truth for request/response shaping — algorithm changes in `src/` require no duplicated adaptation logic across transports.
  * The stateless design for tree structures avoids session lifecycle management (expiry, cleanup, concurrency) at the cost of rebuilding the tree on every call; this is acceptable given these structures are cheap to reconstruct and typically queried a handful of times per request in this context.
  * *Trade-off:* Adding a new transport (e.g., gRPC) or a new algorithm requires touching three files (`tools.py`, `mcp_server.py`, `http_app.py`) instead of one, but keeps each transport's concerns (protocol framing, schema validation) cleanly separated from the algorithm-agnostic adapter logic.
  * Introduces new dependencies (`mcp`, `fastapi`, `uvicorn`, `httpx`) beyond the previously dependency-light `numpy`-only `src/` package; these are isolated to `service/` and its tests, so `src/` remains independently importable without them.

