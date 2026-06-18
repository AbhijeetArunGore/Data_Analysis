nums=[2,7,11,15]
target=int(input("enter number :"))
n=len(nums)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,n):
            for j in range(1,n):
                if(nums[i]+nums[j]==target):
                    return i,j
                else:
                    print("no pair")
s=Solution()
result=s.twoSum(nums,target)
print(result)