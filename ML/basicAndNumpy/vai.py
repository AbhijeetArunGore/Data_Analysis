nums=[2,7,8,5]
target=9

class Solution(object):
   def twoSum(self, nums, target):
        for i in range(len(nums)):  
            for j in range(i + 1, len(nums)):  
                if nums[i] + nums[j] == target:
                    return [i,j]

solution = Solution()
print(solution.twoSum(nums, target))  # Output: (1, 2)
