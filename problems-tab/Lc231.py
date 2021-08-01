class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=0
        value=0
        while value!=n and value<n:
            value=2**num
            num=num+1
        if value==n:
            return True
        return False
obj=Solution()
z=obj.isPowerOfTwo(12)
print(z)

