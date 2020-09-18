class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        i = 0
        met = {}
        for j in range(len(s)):
            if s[j] in met:
                i = max(met[s[j]], i)
            cnt = max(cnt, j - i + 1)
            met.update({s[j]: j + 1})
        return cnt

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 

s = Solution()
# str = "bbbbbb"
# str = "abcabcbb"
str = "pwwkew"
res = s.lengthOfLongestSubstring(str)
print(res)