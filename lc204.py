class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                 a.append(i)
        return len(a)
obj1=Solution()
a=[]
a=obj1.countPrimes(10) 
print(a)