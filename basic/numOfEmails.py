#coding:utf - 8
'''
1.新建一个字典dic.以域名为key，相应的本地名为value.同一域名的本地名保存在一起。新建一个空的列表，通过append将不同的本地名添加在同一个列表中
2. 遍历字典中的每个key,即域名，计算每个域名下有多少个不同的本地名。通过count()实现。
3.count 的 key为有效本地名。根据字典的key具有唯一性，可以过滤掉重复的本地名
4. 该进。过滤掉相同的本地名，可以通过集合实现。
'''
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}
        result = 0
        for email in(emails):
            local,domain = email.split('@')
            if domain not in dic:
                dic[domain] = []
                dic[domain].append(local)

            else:
                dic[domain].append(local)

        for k in dic.keys():
            result += self.count(dic[k])
        return result
    def count(self,locals):
        # print 'locals: ',locals
        l = len(locals)
        dic_locals = {}
        for i in locals:
            if '+' in i:
                i = i.split('+')[0]
            if '.' in i:
                j = i.split('.')
                i = ''.join(part for part in j)

            if i not in dic_locals.keys():
                dic_locals[i] = 1
        r = 0
        for value in dic_locals.values():
            r += value
        # print 'r:',r
        return r





A = Solution()
# b = A.numJewelsInStones(J,S)
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
dic = A.numUniqueEmails(emails)
print dic