from typing import Counter


class Solution:
    def countSegments(self, s: str) -> int:
        # print(len(s))
        res=list(s.split(" "))
        # print(res)
        # print(Counter(s))
        for i in range(len(res)):
            for j in res:
                if j=='' :
                    res.remove(j)
        # print(res)
        # print(Counter(s))
        return len(res)
        
obj=Solution()
print(obj.countSegments("             "))