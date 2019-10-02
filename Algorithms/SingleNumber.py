egList = [4,4,5,5,6,7,8,7,6]

class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for num in nums:
            # .get is used to access elements of the dictionary
            # can't just access elements as easily as lists
            dic[num] = dic.get(num, 0)+1
            
            # .items() returns all key, value pairs in the dictionary
        for key, val in dic.items():
            if val == 1:
                return key

test = Solution()
print(test.singleNumber(egList))