egNumbers = [2,7,11,15]
egTarget = 9

egNumbers2 = [2,3,4]
egTarget2 = 6

class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l <r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else: 
                r -= 1
                
test = Solution()
print(test.twoSum(egNumbers,egTarget))

test2 = Solution()
print(test2.twoSum(egNumbers2, egTarget2))
