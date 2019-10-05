input1 = 1
input2 = 28
input3 = 701


class Solution:
    def convertToTitle(self, num):
        """
        - chr(x) returns unicode character for a given integer x
        - ord is the inverse of chr, so returns integer x for given
          character
        - Here we generate the list of capitals for the range of
          capital letters A-Z
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while num >0:
            # append first letter from A-Z corresponding to input num
            # % is modulus, returns remainder of num/26
            result.append(capitals[(num-1) % 26])
            # floor division (drops any decimal places)
            num = (num-1) // 26
        # Makes sure that 27 is AB not BA for example
        result.reverse()
        # join  the elemnts of the list into a string
        return ''.join(result)

test = Solution()
print(test.convertToTitle(input1))
print(test.convertToTitle(input2))
print(test.convertToTitle(input3))
