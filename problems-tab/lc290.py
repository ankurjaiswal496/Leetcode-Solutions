from collections import Counter


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a=list(pattern)
        b=list(s.split(" "))
        print(a,b)
        
        # for i in pattern:
        #     a.append(i)
        
        
        # res={a[i]:b[i] for i in range(len(pattern))}
        res=dict(zip(b,a))
        a=len(res)
        print(a)
        c=res.count()
        print(c)
obj=Solution()
obj.wordPattern("abba","dog cat cat dogs")

