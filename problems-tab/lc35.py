class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,v in enumerate(nums):
            if v==target:
                return i
            elif v>target :
                return i
            elif nums[len(nums)-1]<target:
                return len(nums)
        
                        

    
obj=Solution()
print(obj.searchInsert([1,3,5,6],7))