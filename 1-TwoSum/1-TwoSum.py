# Last updated: 5/24/2026, 12:31:41 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hash_map = {nums[i]: i for i in range(len(nums))}
4        for i in range(len(nums)):
5            diff = target - nums[i]
6            if diff in hash_map and hash_map[diff] != i:
7                return [i, hash_map[diff]]