class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter

        # b=Counter(nums)
        for a in Counter(nums).values():
            print(b)
            if a>=2:
                return True
            else:return False
        
        
obj= Solution()
print(obj.containsDuplicate([1,2,3,1]))
