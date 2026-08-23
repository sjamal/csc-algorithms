# Computer Science & Software Engineering Algorithms

A structured repository dedicated to implementing, analyzing, and documenting foundational computer science algorithms and data structures using Python. This project serves as an educational sandbox to study runtime complexities, data architecture, and verification methodologies.

## Project Structure

* `src/`: Core Python implementations categorized by algorithmic domain.
* `tests/`: Automated unit tests mirroring the codebase layout to validate edge cases and performance boundaries.
* `docs/adr/`: Architectural Decision Records tracking the design choices for each algorithm.

## Getting Started

### Prerequisites

* Python 3.10 or higher
* pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd csc-algorithms
   ```

2. Initialize a local virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required development and testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Execution and Testing

The repository uses `pytest` for codebase verification. Run the test suite globally using the following command:

```bash
pytest tests/
```

To run syntax and style validation checks using `flake8` or `black`:

```bash
black --check src/ tests/
```

## Architectural Decision Records (ADRs)

The architectural choices, trade-offs, and design patterns for each algorithm are fully documented below:

* [ADR 0001: Hoare Partitioning for Quicksort](docs/adr/0001-use-hoare-partitioning-for-quicksort.md)
* [ADR 0002: heapq for Dijkstra Priority Queue](docs/adr/0002-use-heapq-for-dijkstra-priority-queue.md)
* [ADR 0003: LPS Array for KMP String Matching](docs/adr/0003-use-lps-array-for-kmp-string-matching.md)
* [ADR 0004: Recursive Node-Pointer Binary Search Tree](docs/adr/0004-recursive-node-pointer-binary-search-tree.md)
* [ADR 0005: NumPy Vectorized K-Means Clustering](docs/adr/0005-numpy-vectorized-k-means-clustering.md)
* [ADR 0006: NumPy eigh Covariance PCA](docs/adr/0006-numpy-eigh-covariance-principal-component-analysis.md)
* [ADR 0007: Edge-List Relaxation for Bellman-Ford](docs/adr/0007-use-edge-list-relaxation-for-bellman-ford.md)
* [ADR 0008: Euclidean Heuristic for A* Pathfinding](docs/adr/0008-use-euclidean-heuristic-for-a-star.md)
* [ADR 0009: AVL Rotations for Self-Balancing BST](docs/adr/0009-use-avl-rotations-for-self-balancing-bst.md)

---

## Code Quality and Design Guidelines

### Naming Conventions & Code Style
To ensure uniformity, this repository follows strict standards derived from **PEP 8**:
* **Functions & Variables:** Lowercase word blocks separated by underscores (`snake_case`).
* **Protected Components:** Preceded by a single leading underscore (e.g., `_partition`).
* **Constants:** Full uppercase strings separated by underscores (`UPPER_SNAKE_CASE`).
* **Type Hinting:** Mandatory on all public functions via the `typing` module framework.

### Security, Stability & Privacy Considerations
1. **Input Integrity & Memory Protection:** Sorting algorithms construct a explicit local `list()` copy of tracking variables to prevent input reference mutation bugs.
2. **Denial of Service (DoS) Boundaries:** Quicksort worst-case scaling behavior is $O(n^2)$. For safety-critical systems sorting untrusted or adversarial user inputs, randomizing the pivot selection or utilizing `heap-sort`/`merge-sort` derivatives should be considered.
3. **Graph Payload Resilience:** The Dijkstra parser explicitly references data isolation using explicit `float("inf")` typing arrays. Node configurations must strictly pass hashable unique strings to mitigate graph processing collision events.
4. **Data Isolation:** This package operates entirely locally on internal operational states. No logging pipelines, web tracing, or environment data tracking hooks are implemented, ensuring maximum data privacy.
5. **Negative-Weight Cycle Guarding:** The Bellman-Ford implementation runs an explicit final relaxation pass to detect reachable negative-weight cycles and raises a `ValueError` rather than allowing an untrusted graph payload to loop indefinitely.
6. **Heuristic Input Validation:** The A* implementation validates that source, target, and coordinate metadata exist before search begins, and rejects negative edge weights, preventing malformed spatial graphs from corrupting the heuristic scoring.
7. **Balanced Depth Guarantee:** The AVL Tree rebalances on every insert and delete, preventing adversarial sorted-input sequences from degrading traversal operations to linear time.


