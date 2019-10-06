egnums = [1,2,2,2,2,3,4]

class Solution:
    def MajorityElement(self, num):
        # float division
        return sorted(num)[len(num)//2]

test = Solution()
print(test.MajorityElement(egnums))