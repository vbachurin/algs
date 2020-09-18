class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        i = 0
        a = 1
        d = [[0] for z in range(numRows)]
        print(d)
        if numRows == 1:
            return s
        for c in s:
            d[i] = d[i].append(c)
            if i == numRows - 1:
                a = -1
            if i == 0:
                a = 1
            i += a
        print(d)

        for j in range(numRows):
            res += map(lambda t: t[0], list(filter(lambda t: t[1] == j, d)))
        return ''.join(res)

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# P   A   H   N
# A P L S I I G
# Y   I   R

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

sol = Solution()
s = "AB"
# s = "PAYPALISHIRING"
numRows = 0
res = sol.convert(s, numRows)
print(res)
