from typing import Counter


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a=Counter(s)
        print(a)
        if a.get('A')>2:
            return False
        for c in range(len(s)):
            if s[c]=='L':
                    if s[c+1]=='L':
                        if s[c+2]=='L':
                            return False
        return True

        # c=0
        # c1=0
        # c2=
        # for i in range(len(s)):
        #     if s[i]=='P':
        #         if s[i+1]=='P':
    
obj=Solution()
print(obj.checkRecord("PPAAALL"))