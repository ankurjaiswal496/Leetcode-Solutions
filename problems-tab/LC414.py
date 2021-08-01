class Solution:
    def thirdMax(self, nums) :
         a=set(nums)
         if len(a)<=2:
            return max(nums)  
         a.remove(max((a)))
         
         a.remove(max((a)))

         return max(a)
        
obj=Solution()
print(obj.thirdMax([2,2,3,1]))