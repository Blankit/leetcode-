class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        l = len(J)
        dic = {}
        for i in S:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = 0
        for i in range(l):
            if J[i] in dic:
                result += dic[J[i]]
        return result
J = "aA"
S = "aAAbbbb"
A = Solution()
b = A.numJewelsInStones(J,S)
print b
