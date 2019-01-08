class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = -1
        l = len(nums)
        j = 0
        while j < l:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1,l):
            nums.pop(-1)

        return nums


nums = [3,2,6,4,3,5,7]
val = 3
A = Solution()
b = A.removeElement(nums,val)
print b