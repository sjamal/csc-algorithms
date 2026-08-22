# 1. Use Hoare Partitioning for Quicksort

* **Status:** Approved
* **Context:** Choosing between Lomuto and Hoare partitioning schemes impacts sorting performance on large arrays or arrays with duplicate elements.
* **Decision:** We implemented the **Hoare partition scheme**.
* **Consequences:** 
  * Hoare's scheme makes three times fewer swaps on average compared to Lomuto.
  * It handles arrays with a high volume of duplicate values much more efficiently.
  * *Trade-off:* The implementation is slightly more abstract and non-stable.

