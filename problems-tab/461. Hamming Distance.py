class Solution:
    def hammingDistance(self, x, y) :
        # print(x^y)
        # print(bin(x ^ y))
        return bin(x ^ y).count('1')

obj=Solution()
print(obj.hammingDistance(3,1))