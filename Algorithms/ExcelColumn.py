input1 = 1
input2 = 28
input3 = 701


class Solution:
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while num >0:
            result.append(capitals[(num-1) % 26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

test = Solution()
test.convertToTitle(input1)
test.convertToTitle(input2)
test.convertToTitle(input3)
