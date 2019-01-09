class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l <= 1:
            return False
        dic = {}
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        m = max(dic.values())
        if m >1:
            return True
        else:
            return False
nums = [1,2,3,1]
A = Solution()
b = A.containsDuplicate(nums)
print b
