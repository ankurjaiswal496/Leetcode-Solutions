class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [0,1]
        i = 2
        while i <= n:
            fib.append(fib[i-2] + fib[i-1])
            i += 1
        return fib[n]