class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        l1 = len(nums1)
        l2 = len(nums2)
        if not(l1 and l2):
            return
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while(i<l1 and j< l2):
            if nums1[i] == nums2[j]:
                r.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return r

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
A = Solution()
b = A.intersect(nums1,nums2)
print b

