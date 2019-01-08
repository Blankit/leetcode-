class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 0:
            return 0
        left = 0
        right = l
        s_r = sum(nums[left:right-1])
        while
