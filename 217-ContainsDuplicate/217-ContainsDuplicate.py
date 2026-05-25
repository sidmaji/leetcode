# # Solution 1
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # brute force solution: O(n^2)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] == nums[j] and i != j:
#                     return True
#         return False

# # Solution 2
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # hash map approach (beats 12%)
#         hash_map = {}
#         for i in nums:
#             if i not in hash_map:
#                 hash_map[i] = 0
#             hash_map[i] += 1
#             if hash_map[i] > 1:
#                 return True
#         return False

# Solution 3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)