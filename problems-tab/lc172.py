import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        b=str(math.factorial(n))
       
        count=0
        if  '0' not in  b:
            print("hey1")
            return 0
        
        else :
            count=0
            for i in b[::-1]:
                if i == '0':
                    count+=1
               
                else:break
        print(count)    
            # return b.count(b[-1]) 

obj=Solution()
obj.trailingZeroes(7)