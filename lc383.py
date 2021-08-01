class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a=list(ransomNote)
        b=list(magazine)
        if len(magazine)<len(ransomNote):
            return False
 
        for i in b:         #a
             if b[i] in a:#a
                 b.remove(i) #ab
                 a.remove(i) #a
        print(a)
        print(b)
        if not a  :
            return True
        return False
obj=Solution()
print(obj.canConstruct("aa","aab"))
