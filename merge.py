#coding:utf-8
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        i = 0
        j = 0
        count = 0#从nums2插入到nums1的元素个数
        if len(nums2) == 0:
            return
        while i < l-1:
            while j < n:
                # if (nums2[j]> nums1[i]) & (nums2[j] <= nums1[i+1]):
                if (nums2[j]< nums1[i]):
                    nums1.insert(i,nums2[j])
                    count += 1
                    i = i+1
                    j += 1
                else:
                    j +=1
            j = 0
            i = i +1


        # print 'j:',j
        # print 'count:',count
        if count < n:#nums2中的元素未完全插完，补在nums1后面,还剩n-count个
            for i in range(m +count,m+n):
                nums1[i] = nums2[i-m]
        for i in range(count):
            nums1.pop(-1)
# nums1 = [1,2,3,0]
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
A = Solution()
b = A.merge(nums1,m,nums2,n)
print nums1

