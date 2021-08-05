class Solution:
    def repeatedSubstringPattern(self, s) :
        #  print(len(s)//2)
         for k in range(1, len(s)//2 +1):   
            # print(s[k:] + s[:k])
            if s == s[k:] + s[:k]:
                print(s[k:] + s[:k])
                return True
         return False

obj=Solution()
obj.repeatedSubstringPattern("abab")
        
# s="abab"
# print(s[1:])