class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        a=[]
        while 0 in nums:
        
            a.append(0)
            nums.remove(0)
        for x in a:
            nums.append(x)
        return nums
obj=Solution()
print(obj.moveZeroes([0,0,1]))