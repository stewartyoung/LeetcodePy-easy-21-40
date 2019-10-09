testString1 = "A"
testString2 = "AB"
testString3 = "BD"

class Solution:
    def ExcelColumnNumber(self, string):
        result = 0
        for char in string:
            result = result * 26 + ord(char) - 64
        return result

test = Solution()
print(test.ExcelColumnNumber(testString1))
# test.ExcelColumnNumber(testString2)
# test.ExcelColumnNumber(testString3)