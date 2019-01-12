#coding:utf-8
'''
找出第一次出现True的下标
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version,v=1):
    if version >= v:
        return True
    else:
        return False
    # return version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start<=end:
            if isBadVersion(start):
                return start
            if isBadVersion(end):
                if isBadVersion(end - 1):
                    end -= 1
                else:
                    return end

            mid = (start + end) // 2
            if isBadVersion(mid):
                if (isBadVersion(mid+1) and (not isBadVersion(mid-1))):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
            mid = (start+end)/2
n = 2
A = Solution()
b = A.firstBadVersion(n)
print b



