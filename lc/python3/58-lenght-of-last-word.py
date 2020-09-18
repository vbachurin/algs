class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            if (s[i] == ' ' and l != 0):
                return l
            if (s[i] != ' '):
                l += 1
        return l

s = Solution()
# res = s.lengthOfLastWord("")
res = s.lengthOfLastWord("Hello  World    ! ")
print(res)