from typing import Counter


class Solution(object):
    Counter = 0
    def __init__(self,n):
        Solution.Counter +=1
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in nums:
            if i not in nums[:len(nums)]:
                break
        return i
                
        
obj=Solution(10)
# print(obj.Counter)
obj1=Solution(10)
obj2=Solution(11)
# obj=Solution(12)
print(obj.Counter)
obj.singleNumber(['2'])
print(Solution.Counter)
# print(obj.singleNumber([4,1,2,1,2]))