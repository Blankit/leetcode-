#coding:utf-8
'''
维护一个非0数组，j表示最后一位非0元素的下标
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        j = -1
        for i in range(l):
            if nums[i]:
                j += 1
                nums[j] = nums[i]
        for i in range(j+1,l):
            nums[i] = 0

nums = [0,1,0,3,12]
A = Solution()
b = A.moveZeroes(nums)
print nums

