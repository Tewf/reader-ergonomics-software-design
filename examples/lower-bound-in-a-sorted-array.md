# Lower bound in a sorted array

**Shape:** [algorithm specification](../shapes/algorithm-specification.md)

**Problem.** Find the first position in a sorted array whose value is at least `x`.

**Interface.**
- Input `a`: an array of `n` comparable values, `n` ≥ 0. Input `x`: a value of the same type.
- Output `i`: an integer with 0 ≤ `i` ≤ `n`.

**Contract.**
- Precondition: `a` is sorted in non-decreasing order.
- Postcondition: every `a[j]` with `j` < `i` is less than `x`, and every `a[j]` with `j` ≥ `i` is at least `x`.

**Technique.** Decrease and conquer, halving the interval at each pass, because the order lets one comparison discard
half of what is left.

**Steps.**

    lo ← 0; hi ← n
    while lo < hi:
        mid ← lo + (hi − lo) div 2
        if a[mid] < x: lo ← mid + 1
        else: hi ← mid
    return lo

**Invariants.**
- The loop: 0 ≤ `lo` ≤ `hi` ≤ `n`; every `a[j]` with `j` < `lo` is less than `x`; every `a[j]` with `j` ≥ `hi`
  is at least `x`. Variant: `hi − lo` strictly decreases, since `mid` lies in [`lo`, `hi`). At exit `lo` = `hi`, and
  the invariant gives the postcondition.

**Cost.** At most ⌈log₂(`n` + 1)⌉ passes, so time O(log `n`) in the length of `a`; space O(1).

**Examples.**

| Input `a`, `x` | Expected `i` | Why this case |
|---|---|---|
| [], 5 | 0 | empty array |
| [1, 3, 3, 7], 0 | 0 | every value at least `x` |
| [1, 3, 3, 7], 9 | 4 | every value less than `x` |
| [1, 3, 3, 7], 3 | 1 | duplicates: the first of them |
| [1, 3, 3, 7], 4 | 3 | `x` absent: where it would go |

**Properties.**
- `i` equals the number of values in `a` less than `x`.
- Inserting `x` at position `i` keeps `a` sorted.

**Plan.**
1. Write the five examples as tests.
2. Implement the loop with the invariant as an assertion in a debug build.
3. Test both properties on random sorted arrays against a linear scan.
4. Keep `mid` as `lo + (hi − lo) div 2`, which cannot overflow in fixed-width integers.

**Out of scope.**
- Unsorted input: the precondition is not checked, since checking it costs O(`n`).
- A flag saying whether `x` was found.

**Open questions.** None.

The examples, both properties and the bound on passes were run before publication: 20,000 random cases with arrays of
up to 64 values.
