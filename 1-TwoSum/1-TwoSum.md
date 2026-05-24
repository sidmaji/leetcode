---
link: https://leetcode.com/problems/two-sum/
difficulty: Easy
topics:
  - array
  - junior
  - hash-table
---
# TwoSum

## Approach
Initialize an empty hash map (or dictionary in Python). Looping through the **nums** list, check if the difference between the target sum and the current number is present as a key in the hash map. If it is, that means the remaining number needed to achieve the target sum exists in **nums**. Then, return a list with the current index and the index of the difference number, which will be stored as a value in the hash map. Usually, when the current index does not have the necessary value to get the target sum, the current number will be stored in the hash map, with its value being the index.

## Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [i, hash_map[target - num]]
            hash_map[num] = i
```

## Complexity
Time Complexity: O(n)
Space Complexity: O(n)