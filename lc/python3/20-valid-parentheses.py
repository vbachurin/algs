class Solution:
    stack = []
    result = True  
    def isValid(self, s: str) -> bool:
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                self.stack.append(c)
                self.result = False
            elif (c == ')' and self.peek() == '('):
                self.popAndTrue()
            elif (c == ']' and self.peek() == '['):
                self.popAndTrue()
            elif (c == '}' and self.peek() == '{'):
                self.popAndTrue()
            else:
                return False
        if (len(self.stack) == 0):
            return self.result
        else:
            return False

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def popAndTrue(self):
        self.result = True
        return self.stack.pop()

s = Solution()
result = s.isValid("{[]}")
print(result)