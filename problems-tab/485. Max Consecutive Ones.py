from typing import Counter


class Solution:
    def findMaxConsecutiveOnes(self, nums) :
        count=0
        count1=0
        for i in nums:
            if i==1:
                count+=1 
            else:
                count=0
            if count1<count:
                count1=count
        return count1
        
        
        
obj=Solution()
print(obj.findMaxConsecutiveOnes([1,1,1,0,1,1]))