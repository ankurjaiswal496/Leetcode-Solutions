class Solution:
    def vowelreverse(self,s):
        a=[]
        for i in s:
            if i in ['a','e','i','o','u']:
                a.append(i)
                s=s.replace(i,'_')
        a.reverse()
        for j in a:
            s=s.replace('_',j,1)
        return s

obj=Solution()
print(obj.vowelreverse("hello"))

