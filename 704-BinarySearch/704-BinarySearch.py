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