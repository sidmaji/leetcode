# Last updated: 4/19/2026, 2:38:44 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # brute force solution: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and i != j:
        #             return True
        # return False

        # # hash map approach (beats 12%)
        # hash_map = {}
        # for i in nums:
        #     if i not in hash_map:
        #         hash_map[i] = 0
        #     hash_map[i] += 1
        #     if hash_map[i] > 1:
        #         return True
        # return False

        # use hash set, O(n) time complexity
        return len(set(nums)) < len(nums)