class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        i = 0
        j = l - 1
        dic = {}
        for element in nums:
            if element in dic:
                dic[element] = [i]
            else:
                dic[element].append(i)
            i += 1
        # print dic
        i = 0
        nums.sort()
        while i<j:
            temp = nums[i] + nums[j]
            if temp == target:
                return [dic[nums[i]],dic[nums[j]]]
            elif temp > target:
                j -= 1
            else:
                i += 1
        return
nums = [3,2,5]
target = 8
A = Solution()
b = A.twoSum(nums,target)
print b
