class Solution(object):

    def convertToTitle(self, n):
            res = []
            a = ord('A')
            while(n > 0):
                x = (n - 1) % 26
                res.append(chr(x + a))
                n = (n - 1) // 26
                print(f"x = {x}, n = {n}")
            res.reverse()
            return ''.join(res)



# Input: 1
# Output: "A"

# Input: 28
# Output: "AB"

# Input: 701
# Output: "ZY"        

s = Solution()
n = 701
res = s.convertToTitle(n)
print(res)

# print(chr(1 + 64))