class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            print(f"numbers[{i}] = {numbers[i]}, numbers[{j}] = {numbers[j]}")
            sum = numbers[i] + numbers[j] 
            if (sum > target): j -= 1
            elif (sum < target): i += 1
            else: break
        return [i + 1, j + 1]

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.        

s = Solution()
numbers = [2,7,11,15]
target = 9
res = s.twoSum(numbers, target)
print(res)