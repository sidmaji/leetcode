---
link: https://leetcode.com/problems/first-missing-positive/
difficulty: Hard
topics:
  - array
  - hash-table
---
# First Missing Positive

## Approach
The `nums` list is converted into a hash set and stored in `nums_set`. Python makes this very simple through the `set()` function.

A counter `i` is initialized as `1`, because that is the first possible positive. That counter is iterated until it is no longer a value present in `nums_set`. Since it is a hash set, it has no duplicate values and values can be referenced O(1).

Finally, the counter is returned, representing the first positive that is missing from the deduplicated set version of `nums`.

## Solution
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        i = 1
        while i in nums_set:
            i += 1
        return i
```

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)