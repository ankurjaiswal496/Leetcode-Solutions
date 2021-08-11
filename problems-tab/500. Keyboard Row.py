class Solution(object):
    def findWords(self, words):
        """
        :type words: set[str]
        :rtype: set[str]
    
        """
        a=set("qwertyuiop")
        b=set("asdfghjkl")
        c=set("zxcvbnm")
        d=[]
        # print
        # count=count1=count2=0
        for i in words:
            w=set(i.lower())
            if w&a==w or w&b==w or w&c==w:
                d.append(i)
        return d

obj=Solution()
words=["Hello","Alaska","Dad","Peace"]
print(obj.findWords(words))