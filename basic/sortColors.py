#coding:utf-8
'''
1. 这是基数排序吗？中间的过程觉得很傻
2. 考虑用快排，但是只用一次快排不能得出结果。等于1的无法排
3. 官方给的答案用的是三路快排

'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        #将值为1的数放在第一位
        dic = {}
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] +=1
        # print "dic: ",dic
        if 0 in dic:
            num0 = dic[0]
            for k in range(num0):
                nums[k] = 0
        else:
            num0 = 0
        if 1 in dic:
            num1 = dic[1]
            for k in range(num0, num0 + num1):
                nums[k] = 1
        else:
            num1 = 0
        for k in range(num0 + num1, l):
            nums[k] = 2

nums = [0]
A = Solution()
b = A.sortColors(nums)
print nums


