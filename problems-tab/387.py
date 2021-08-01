from typing import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res=Counter(s)
        # print(res['l'])

        for i in res.keys():
            # print(res[i])
            if res[i] == 1:
                print(s.index(i))
                return s.index(i)
        return -1      
         

obj=Solution()
print(obj.firstUniqChar("leetcode")) 