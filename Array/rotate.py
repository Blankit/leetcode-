#coding:utf-8
'''
使用pop弹出最后一个数
将弹出的数始终插在列表的头部
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop(-1))
nums = [1,2,3,4,5,6,7]
k = 3
A = Solution()
b = A.rotate(nums,k)
print nums