class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for x in t:
            if x not in s:
                return x
            s=s.replace(x,'_',1)
            # print(s)

obj=Solution()
obj.findTheDifference('ae','aea')