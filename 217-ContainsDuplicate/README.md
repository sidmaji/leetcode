---
link: https://leetcode.com/problems/contains-duplicate/
difficulty: Easy
topics:
  - array
  - hash-table
  - sorting
---
# Contains Duplicate

## Approach
Check if the length of the set of `nums` is shorter than the length of `nums`. If it is, that means there were duplicates in `nums`.

## Solution
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)