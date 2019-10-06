testString1 = "A"
testString2 = "AB"
testString3 = "BD"

class Solution:
    def ExcelColumnNumber(self, string):
        return ord(string)//26 - 1

test = Solution()
print(test.ExcelColumnNumber(testString1))
# test.ExcelColumnNumber(testString2)
# test.ExcelColumnNumber(testString3)