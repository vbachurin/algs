class Solution:
    def intToRoman(self, num: int) -> str:
        num0 = num
        result = []
        tuples = [(1000, 100), (500, 100), (100, 10), (50, 10), (10, 1), (5, 1), (1, 0)]
        romans = [('M', 'C'), ('D', 'C'), ('C', 'X'), ('L', 'X'), ('X', 'I'), ('V', 'I'), ('I', '')]
        i = 0
        while i < len(tuples):
            if num0 >= tuples[i][0]:
                num0 -= tuples[i][0]
                result.append(romans[i][0])
            elif num0 >= (tuples[i][0] - tuples[i][1]):
                num0 -= (tuples[i][0] - tuples[i][1])
                result.append(romans[i][1])
                result.append(romans[i][0])
            else:
                i += 1
        return "".join(result)


# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

s = Solution()
num = 1994
res = s.intToRoman(num)        
print(res)