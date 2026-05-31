---
link: https://leetcode.com/problems/binary-search/
difficulty: Easy
topics:
  - array
  - binary-search
---
# Binary Search

## Approach
Initialize `start` and `end` variables which will indicate the starting and ending index of the current search space.

In binary search, the search space is always getting cut in half, and I can use a binary search algorithm because `nums` is sorted.

Looping until `start > end`, I check the midpoint index which I can get by averaging the starting and ending indices and flooring them by using integer division `//`. I then check this index to see if it matches the `target`. If not, I check if it's less than or greater than `target`.

If less than, that means the indices $\le$ the current `i` are guaranteed to not be the `target` number, so the `start` index is shifted to 1 right of `i`. Similarly, if greater than, everything that comes after the current `i` cannot be `target`, so `end` is shifted to 1 left of `i`.

Finally, if the `target` was not found, `-1` is returned.

## Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            i = (end + start) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                start = i + 1
            else:
                end = i - 1
        return -1
```

## Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)