class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        for s in zip(*strs):
            if (len(set(s)) == 1):
                res+=s[0]
            else:
                break
        return res

s = Solution()
res = s.longestCommonPrefix(["flower","flow","flight"])
print(res)
