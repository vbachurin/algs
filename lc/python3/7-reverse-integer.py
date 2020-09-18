import sys
print(sys.version)
from math import pow

class Solution:

    def __recur(self, x: int) -> list:       
        if (x < 10):
            if (x == 0): 
                return [] 
            else: 
                return[str(x)]

        else:
            list1 = [str(x % 10)] + self.__recur(x // 10)
            return list1

    def reverse(self, x: int) -> int:
        list1 = self.__recur(abs(x))
        if not list1:
            return 0
        y = int("".join(list1))
        if (abs(y) > pow(2, 31)):
            return 0
        if (x < 0): 
            return -y
        else:    
            return y



s = Solution()
print(s.reverse(0))