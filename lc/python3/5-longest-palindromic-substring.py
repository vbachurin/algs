class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [x for x in s]

        def pal(p: int, l: int, r: int, res: str) -> str:
            while p-l >= 0 and p+r < len(s):
                if s[p-l] == s[p+r]:
                    res = f"{s[p-l]}{res}{s[p+r]}"
                else:
                    return res
                l += 1
                r += 1
            return res

        for i in range(1, len(s)):
            curr = ""
            if s[i-1] != s[i]:
                curr = pal(i, 1, 1, f"{s[i]}")
            else:
                curr1 = pal(i, 1, 1, f"{s[i]}")
                curr2 = pal(i, 2, 1, f"{s[i-1]}{s[i]}")
                curr = curr1 if len(curr1) > len(curr2) else curr2
            dp[i] = curr if len(curr) > len(dp[i-1]) else dp[i-1]
        return dp[-1] if dp else ""

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

s = Solution()
str = "cabbad"
# str = "ccccc"
# str = "babad"
# str = ""
res = s.longestPalindrome(str)
print(res)