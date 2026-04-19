# Last updated: 4/19/2026, 2:38:42 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map and hash_map[difference] != i:
                return [i, hash_map[difference]]