class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)+1):
            print(i)
            if i not in nums:
                print(i)
                return i
        if nums:return max(nums)+1
obj=Solution()
print(obj.missingNumber([0,1]))