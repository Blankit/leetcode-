#coding:utf-8
'''
快排
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums,k):
            start = 0
            end = len(nums) - 1
            t = nums[0]
            while start < end:

                if nums[start] <= t:
                    if nums[end] > t:
                        nums[start], nums[end] = nums[end], nums[start]
                        start += 1
                        end -= 1
                    else:
                        end -= 1
                else:
                    start += 1
            nums[0], nums[start] = nums[start], nums[0]
            return start

        r = partition(nums,k)
        print k
        while r!=k:
            if r<k:
                partition(nums[r:],k-r)
            if r>k:
                partition(nums[:r],r-k)
        return nums[r]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
A = Solution()
b = A.findKthLargest(nums,2)
print nums
print b
