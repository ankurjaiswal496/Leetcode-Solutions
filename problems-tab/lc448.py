class Solution:
    def findDisappearedNumbers(self, nums):
        # print(set(range(1,len(nums)+1)))
        # print(set(nums))
        return set(range(1,len(nums)+1)) - set(nums)
        

obj=Solution()
print(obj.findDisappearedNumbers([1,1]))