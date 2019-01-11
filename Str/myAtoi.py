#coding:utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
#判断是否为空
#strip('str')移除字符串首尾制定字符
        str = str.strip(' ')
        if not str:
            return 0
#         str = str.split()
#取出非空字符串部分
        for index,char in enumerate(str):
            if char==' ':
                str = str[:index]
                break

        if (str[0] not in '-+0123456789'):
            return 0

        l = len(str)
        for i in range(1,l):#判断首位后面是不是数字
            # if not str[i].isdigit():
            if str[i] not in '0123456789':
                str = str[:i]
                break
        if str in '-+':
            return 0
        if int(str)> 2147483647:
            return 2147483647
        if int(str)< -2147483648:
            return -2147483648
        else:
            return int(str)

# str = "-1234ee"
# str = "-"
# str = " "
str = "-+1"
# str = "+1"
A = Solution()
b = A.myAtoi(str)
print b