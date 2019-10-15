def RecursiveFactorial(num):
    if num <=1:
        return num
    else:
        return num * RecursiveFactorial(num - 1)

def IterativeFactorial(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial * i
    return factorial

class Solution:
    def TrailingZero(self, num):
        zeroCount = 0
        if num == 0:
            return zeroCount
        testNumber = str(IterativeFactorial(num))
        i = 1
        while testNumber[-i] == '0':
            zeroCount = zeroCount + 1
            i = i + 1
        return zeroCount

print("example answer of the recursive factorial function for 7 is {}".format(RecursiveFactorial(7)))

test = Solution()
print(test.TrailingZero(9057))