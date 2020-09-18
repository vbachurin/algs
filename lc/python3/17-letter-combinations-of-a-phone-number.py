class Solution:
    mappings = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits: str):
        if not digits or "1" in digits:
            return []
        elif len(digits) == 1:
            return [i for i in self.mappings[digits[0]]]
        else:
            return self.lc(digits)

    def lc(self, digits: str):        
            return [i + "".join(j) for i in self.mappings[digits[0]] for j in self.letterCombinations(list(digits)[1:])]

s = Solution()
digits = "22"
res = s.letterCombinations(digits)
print(res)
# lst = s.letterCombinations([])
# lst.append("4")
# print(lst)