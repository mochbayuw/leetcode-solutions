class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            sisa = target - num
            if sisa in seen:
                return [seen[sisa], i]
            seen[num] = i

