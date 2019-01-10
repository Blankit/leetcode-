class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for index,num in enumerate(s):
            if dic[num] == 1:
                return index
        return -1
s = "loveleetcode"
A = Solution()
b = A.firstUniqChar(s)
print b

