class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        # l = len(nums)
        # if l == 0:
        #     return 0
        # if l == 1:
        #     return nums[0]

        sum_temp = nums[0]
        for i in nums[1:]:
            sum_temp += i
            sum_temp = max(sum_temp,i)
            max_sum = max(max_sum,sum_temp)
        return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
A = Solution()
b = A.maxSubArray(nums)
print b

