#coding:utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if not l:
            return ''
        min_l = len(strs[0])#r如果l==0,则不存在strs[0].list index out of range
        for i in strs:#求数组长度最小的字符串
            l_i = len(i)
            if not l_i:
                return ''
            if l_i<min_l:
                min_l = l_i
        if not min_l:#判断是否有空字符串
            return ''
        flag = 0

        for i in range(min_l):
            for j in range(1, l):
                if strs[0][i] != strs[j][i]:
                    flag = 1

                    break

            if flag:
                r = i
                break
            else:
                r = i+1
        return strs[0][:r]


strs =["dog","racecar","car"]
# strs =['','']
# strs =["aa","a"]
# strs = ["flower","flow","floght"]

A = Solution()
b = A.longestCommonPrefix(strs)
print b


