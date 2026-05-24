# # Solution 1
# # Time: O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if num1 + num2 == target and i != j:
#                     return [i, j]

# # Solution 2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {nums[i]: i for i in range(len(nums))}
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in hash_map and hash_map[diff] != i:
#                 return [i, hash_map[diff]]

# Solution 2 Improved
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [i, hash_map[target - num]]
            hash_map[num] = i