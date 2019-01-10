class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        i = 0
        j = i + 1
        # j = l - 1
        # dic = {}
        while i < l-1:
            while j < l:
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    j += 1

            i += 1
            j = i + 1


nums = [3,2,4]
target = 6
A = Solution()
b = A.twoSum(nums,target)
print b
