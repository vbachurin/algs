class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (not needle):
            return 0
        i = j = 0
        res = -1
        while (i < len(haystack)):
            if (i + len(needle) - j  > len(haystack)):
                return -1
            if (haystack[i] == needle[j]):
                if (j == 0):
                    res = i
                if (j == len(needle) - 1):
                    return res
                j += 1
            else:
                i = res if (res != -1) else i
                j = 0
                res = -1
            i += 1
        return res
s = Solution()
# res = s.strStr("hello","llu")
# res = s.strStr("aaa","aaaa")
# res = s.strStr("aaa","aaa")
# res = s.strStr("ississip","issip")
# res = s.strStr("mississippi","sipp")
print(res)

        # if (not needle):
        #     return 0
        # j = 0
        # res = -1
        # for i in range(len(haystack)):
        #     if (i + len(needle) > len(haystack) and res == -1):
        #         print(f"because ({i + len(needle)} > {len(haystack)})")
        #         return -1
        #     print(f"haystack[{i}] == needle[{j}], {haystack[i]} == {needle[j]}, res = {res}")
        #     ne = (len(needle) - 1) - j
        #     he = i + ne - j
        #     print(f" and  haystack{[he]} == needle{[ne]}, he = {i} + {ne}")
        #     print(f"  {haystack[he]} == {needle[ne]}")            
        #     if (he > len(haystack)):
        #         return -1
        #     if (haystack[i] == needle[j] and haystack[he] == needle[ne]):
        #         if (j == 0):
        #             print(f"reassigned res = {i}")
        #             res = i
        #         if (j >= ne):
        #             return res
        #         j += 1  
        #     else:
        #         j = 0
        #         res = -1
        #     print()
        # return -1

