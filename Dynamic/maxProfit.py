#coding:utf-8
'''
遍历数组时，没次保存最大的利益和最小的售价
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        profit = 0
        l = len(prices)
        for i in range(1,l):
            if prices[i] < prices[left]:
                left = i
            profit = max(profit,prices[i] - prices[left])
        return profit
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
prices = []
A = Solution()
b = A.maxProfit(prices)
print b

