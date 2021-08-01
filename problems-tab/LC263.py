class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=int(n)
        for i in range(2, n + 1):
            if(n % i == 0):
                isprime = 1
                for j in range(2, (i //2 + 1)):
                    if(i % j == 0):
                        isprime = 0
                        break
                
                if (isprime == 1):
                    print(" %d is a Prime Factor of a Given Number %d" %(i, n))
obj=Solution()
obj.isUgly(8)
