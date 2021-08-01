class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=nums[:]
        while val  in nums:
             nums.remove(val)
             print(nums)
        return len(nums)
obj=Solution()
print(obj.removeElement([3,2,2,3],3))
                
        