#coding:utf-8
'''
暴力
时间复杂度O(kn)
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(l-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = temp

nums = [1,2,3,4,5,6,7]
k = 3
A = Solution()
b = A.rotate(nums,k)
print nums