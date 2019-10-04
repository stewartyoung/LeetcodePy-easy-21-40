egNumbers = [2,7,11,15]
egTarget = 9

class Solution:
    def twoSum(self, numbers, target):
        for num in range(len(numbers)):
            index1 = num
            for i in range(index1 + 1,len(numbers)-1):
                if numbers[index1] + numbers[i] == target:
                    index2 = i
                    return [index1 + 1, index2 + 1]

test = Solution()
print(test.twoSum(egNumbers,egTarget))
