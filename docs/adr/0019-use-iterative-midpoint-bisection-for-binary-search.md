# 19. Use Iterative Midpoint Bisection for Binary Search

* **Status:** Approved
* **Context:** Phase 6 required a foundational $O(\log n)$ lookup mechanism as a baseline searching primitive, applicable whenever data is already sorted (as opposed to linear O(n) scanning).
* **Decision:** We implemented **Binary Search** iteratively, using `low + (high - low) // 2` to compute the midpoint (rather than `(low + high) // 2`) and narrowing the search window each iteration based on comparison against the target.
* **Consequences:**
  * Achieves $O(\log n)$ time and $O(1)$ space, since the iterative approach avoids any recursive call-stack growth.
  * The `low + (high - low) // 2` midpoint formula is a defensive habit carried over from languages with fixed-width integers (where `low + high` can overflow); it is unnecessary in Python's arbitrary-precision integers but costs nothing and keeps the implementation portable as a reference pattern.
  * *Trade-off:* The function assumes its input is already sorted and provides no validation of that precondition — enforcing sortedness would cost an extra $O(n)$ pass, defeating the purpose of using binary search in the first place. Callers are responsible for ensuring sorted input.

