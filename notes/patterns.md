# DSA Problem Patterns 🧠

A concise reference guide to core patterns encountered during LeetCode problem solving. Each pattern breaks down recognition triggers, fundamental concepts, typical complexities, and classic applications.

---

## 1. Hash Map: Complement Lookup

### Use When:
- Searching for pairs or elements that satisfy a condition (e.g., $a + b = \text{target}$)
- Needing $O(1)$ amortized lookup to eliminate nested loops ($O(n^2) \to O(n)$)
- Tracking frequency or previous indices of elements as you traverse

### Basic Idea:
Maintain a hash map storing elements (or their indices) seen so far. At each step, compute the needed complementary value (`target - current`) and check if it already exists in the map.

### Typical Complexity:
- **Time**: $O(n)$ — Single pass through the array.
- **Space**: $O(n)$ — Stores up to $n$ elements in the dictionary.

### Example Problems:
- LeetCode #1: Two Sum
- LeetCode #217: Contains Duplicate
- LeetCode #560: Subarray Sum Equals K

---

## 2. Linked List: Dummy Head & Carry Simulation

### Use When:
- Building or modifying a linked list where the head node might change or is dynamically computed
- Performing arithmetic operations digit-by-digit across nodes
- Handling edge cases (e.g., empty lists, unequal lengths, trailing carry/overflow)

### Basic Idea:
Initialize an empty sentinel node `dummy = ListNode(0)`. Build the result by attaching nodes to `curr.next`. This eliminates conditional branches for setting up the initial head node. When processing sums, propagate the carry (`carry = total // 10`) until both node pointers and the carry are exhausted. Always return `dummy.next`.

### Typical Complexity:
- **Time**: $O(\max(m, n))$ — Traverses the length of the longer list.
- **Space**: $O(\max(m, n))$ — Produces a new list of at most $\max(m, n) + 1$ nodes.

### Example Problems:
- LeetCode #2: Add Two Numbers
- LeetCode #21: Merge Two Sorted Lists
- LeetCode #445: Add Two Numbers II

---

## 3. Math: Integer Digit Extraction & Half-Reversal

### Use When:
- Checking palindromic properties of numbers without allocating memory for string conversions
- Reversing digits of integers while guarding against 32-bit integer overflow
- Constraints disallow $O(n)$ extra space

### Basic Idea:
Extract digits from the right using modulo (`x % 10`) and reduce the number with integer division (`x //= 10`). Reconstructing only the second half of the number (`while x > reversed_half`) prevents integer overflow. For odd-length numbers, discarding the middle digit via `reversed_half // 10` restores balance.

### Typical Complexity:
- **Time**: $O(\log_{10}(n))$ — Digits are halved in each step.
- **Space**: $O(1)$ — Only a few primitive integer registers.

### Example Problems:
- LeetCode #9: Palindrome Number
- LeetCode #7: Reverse Integer
- LeetCode #231: Power of Two

---

## 4. Strings: Right-to-Left Traversal with State

### Use When:
- Processing strings where a character's value depends on subsequent characters (e.g., Roman numeral subtractive notation like `IV` or `IX`)
- Evaluating expressions or parsing tokens from right to left to simplify lookahead logic

### Basic Idea:
Traversing from right to left avoids boundary checking for the "next" character. Maintain the value of the most recently processed symbol (`prev_value`). If the current symbol has a smaller value than `prev_value`, it represents a subtractive prefix (subtract it from the total); otherwise, add it and update `prev_value`.

### Typical Complexity:
- **Time**: $O(n)$ — Single linear scan over the string.
- **Space**: $O(1)$ — Fixed-size mapping table and accumulator variables.

### Example Problems:
- LeetCode #13: Roman to Integer
- LeetCode #12: Integer to Roman
- LeetCode #14: Longest Common Prefix

---

## 5. Two Pointers (Reference)

### Use When:
- Working with sorted arrays or sequences
- Comparing elements from opposite ends (inward traversal)
- Finding pairs with bounded constraints or partitioning arrays

### Basic Idea:
Initialize two index pointers (e.g., `left = 0`, `right = len(arr) - 1`) and move them toward each other based on comparison conditions until they meet.

### Typical Complexity:
- **Time**: $O(n)$
- **Space**: $O(1)$

### Example Problems:
- LeetCode #167: Two Sum II - Input Array Is Sorted
- LeetCode #11: Container With Most Water
- LeetCode #15: 3Sum
- LeetCode #125: Valid Palindrome
