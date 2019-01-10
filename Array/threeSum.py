class Solution(object):
    def twoSum(self, nums2, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums2)
        i = 0
        j = i + 1
        dic = {}
        print nums2
        for index,num in enumerate(nums2):
            # print index,num
            num2 = target - num
            if num2 in dic:
                return [num2,num]
            else:
                dic[num] = index
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = []
        for index,num1 in enumerate(nums):
            temp = self.twoSum(nums[index+1:],-1*num1)
            if temp:
                r.append([num1] + temp)
        return r

nums = [-1, 0, 1, 2, -1, -4]
A = Solution()
b = A.threeSum(nums)
print b
