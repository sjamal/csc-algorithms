# 22. Use a Character-Branching Trie for Prefix Lookups

* **Status:** Approved
* **Context:** Phase 6 required exact word lookup and autocomplete-style prefix queries. A character-indexed structure should avoid scanning every stored word for each prefix request.
* **Decision:** We implemented a **Trie** whose nodes map characters to child nodes and mark complete words. Exact lookup and prefix existence walk the relevant character path; autocomplete recursively collects descendants and sorts child keys for deterministic suggestions.
* **Consequences:**
  * Insert and exact/prefix lookup take $O(L)$ time for a word or prefix of length $L$.
  * The structure uses space proportional to the number of stored character positions.
  * Autocomplete returns deterministic lexical ordering, while duplicate inserts remain idempotent.
