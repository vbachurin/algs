class Solution:
    def myAtoi(self, str: str) -> int:
        neg = False
        digitsStarted = False
        res = 0
        maxint = pow(2, 31) - 1
        for c in str:
            if c >= '0' and c <= '9':
                digitsStarted = True
                res = res * 10 + int(c)
                if res > maxint:
                    return -maxint - 1 if neg else maxint
            else:
                if not digitsStarted and c == ' ':
                    continue
                elif not digitsStarted and c == '+':
                    digitsStarted = True
                elif not digitsStarted and c == '-':
                    digitsStarted = True
                    neg = True
                else:
                    break
        return -res if neg else res


# Input: "42"
# Output: 42

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

s = Solution()
str = " -42"
# str = " 4193 with words"
# str = " +91283472332 12"
# str = "  words and 987"
# str = "3.14159"
# str = ".1" 
# str = "- 1"
str = "-2147483648"
res = s.myAtoi(str)
print(res)