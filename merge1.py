class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        r = []
        while ((i < m) &(j<n)):
            if nums1[i] < nums2[j]:
                tmp = nums1[i]
                i += 1
            else:

                tmp = nums2[j]
                j += 1

            r.append(tmp)
        if i < m:
            for k in range(i,m):
                r.append(nums1[k])
        if j < n:
            for k in range(j, n):
                r.append(nums2[k])
        for i in range(m+n):
            nums1[i] = r[i]
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
A = Solution()
b = A.merge(nums1,m,nums2,n)
# print nums1
