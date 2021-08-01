class Solution:
    def longsub(self,strs):
        
        final=""
        for j in range(len(strs[0])):
            
            for i in strs:
                
                if strs[0][:j] not in i:
                    return final
            final=strs[0][:j]
        return final
objs=Solution()
strs = ["flower","flow","flight"]
a=objs.longsub(strs)
print(a)
# a="123456"
# print(a[1:])
