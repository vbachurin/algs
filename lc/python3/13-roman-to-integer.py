class Solution:
    def romanToInt(self, s: str) -> int:
        prev = None
        sum = 0
        for c in s:
            if (c == 'I'):
                sum+=1
            elif (c == 'V'):
                if (prev == 'I'):
                    sum-=2
                sum+=5
            elif (c == 'X'):
                if (prev == 'I'):
                    sum-=2
                sum+=10
            elif (c == 'L'):
                if (prev == 'X'):
                    sum-=20
                sum+=50
            elif (c == 'C'):
                if (prev == 'X'):
                    sum-=20
                sum+=100
            elif (c == 'D'):
                if (prev == 'C'):
                    sum-=200
                sum+=500
            elif (c == 'M'):
                if (prev == 'C'):
                    sum-=200
                sum+=1000
            prev = c
        return sum

    # switcher = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000
    # }
    # I -> V, X
    # X -> L, C
    # C -> D, M

s = Solution()
res = s.romanToInt("CMIV")
print(res)