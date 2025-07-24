class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if abs(target - total) < abs(target - closest):
                    closest = total
                    
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # perfect match!
        
        return closest
