class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = 0
        res = []
        l = max(len(a), len(b)) + 1
        for i in range(1, l):
            aa = a[-i] if (len(a) - i >= 0) else 0
            bb = b[-i] if (len(b) - i >= 0) else 0
            s = int(aa) + int(bb) + n
            print(f"{aa} + {bb} + {n} = {s} ({n})")
            if (s == 2):
                s = 0
                n = 1
            elif (s == 3):      
                s = 1
                n = 1
            else:
                n = 0
            res.insert(0, str(s))
        if (n == 1): res.insert(0, '1')
        return ''.join(res)

s = Solution()
res = s.addBinary("1111", "1111")
# res = s.addBinary("1010", "1011")
print(res)

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         n = 0
#         res = []
#         for i in range(1, min(len(a), len(b)) + 1):
#             if (int(a[-i]) + int(b[-i]) + n > 1):
#                 s = 0
#                 n = 1
#             else:
#                 s = int(a[-i]) + int(b[-i]) + n
#                 n = 0
#             print(f"{a[-i]} + {b[-i]} + {n} = {s} ({n})")
#             res.insert(0, s)
#         if (n == 1): res.insert(0, n)
#         return res 
