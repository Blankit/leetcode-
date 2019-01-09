a = [2, 7, 11, 15]
dic = {}
i = 0
for element in a:
    dic[element] = i
    i += 1
print dic
a = dic.keys()
print a.sort()
