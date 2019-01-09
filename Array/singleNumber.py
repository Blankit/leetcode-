class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        r = 0
        for i in range(l):
            r ^= nums[i]
        return r
nums = [4,1,2,1,2]
A = Solution()
b = A.singleNumber(nums)
print b


