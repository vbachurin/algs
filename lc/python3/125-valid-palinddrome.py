import re, string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        ss = pattern.sub('', s).lower()
        result = True
        print(ss)
        for i in range(len(ss) // 2):
            print(f"{ss[i]}[{[i]}] {ss[len(ss) - 1 - i]}[{[len(ss) - 1 - i]}]")
            result = ss[i] == ss[len(ss) - 1 - i]
            if not result: return result
        return result

sol = Solution()
# s = "allaa"
s = "A man, a plan, a canal: Panama"
# s = ",; W;:GlG:;l ;,"
res = sol.isPalindrome(s)
print(res)