testString1 = "A"
testString2 = "AB"
testString3 = "BD"

class Solution:
    def ExcelColumnNumber(self, string):
        nums = []
        for char in string:
            nums.append(ord(char)//26 - 1)
        return ''.join(str(x) for x in nums)

test = Solution()
print(test.ExcelColumnNumber(testString1))
# test.ExcelColumnNumber(testString2)
# test.ExcelColumnNumber(testString3)