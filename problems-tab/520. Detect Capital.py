class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # if len(word)==1:
        #     return True
        if word==word.lower():
            return True
        if word[0]==word[0].capitalize():
            if word[1:]==word[1:].lower():
                return True
        for i in word:
            if i !=i.capitalize():
                return False
        return True


        
obj=Solution()
print(obj.detectCapitalUse("USA"))