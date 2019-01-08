#coding:utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return l
        j = 0
        flag = 0#表示相同的次数，当相同次数小于2时，保存结果，否则，你不保存，相当于一个偏移量
        for i in range(1,l):
            if nums[i] != nums[j]:
                j = j + 1
                nums[j] = nums[i]
                flag = 0
            else:
                flag += 1#累积相同的数字出现的次数
                if flag < 2:#次数少于2，保存在数组中
                    j += 1
                    nums[j] = nums[i]
        for i in range(j+1,l):
           nums.pop(-1)
        return j+1


nums = [0,0,1,1,1,1,2,3,3]
A = Solution()
b = A.removeDuplicates(nums)
print b
print nums