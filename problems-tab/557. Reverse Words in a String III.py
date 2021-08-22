class Solution:
    def reverseWords(self, s: str) -> str:
        a=list(s.split(" "))
        c=" ".join(str(x[::-1]) for x in a)
        return c

obj=Solution()
print(obj.reverseWords("Let's take LeetCode contest"))
