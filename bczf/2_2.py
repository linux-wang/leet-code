# -*- coding:utf-8 -*-
# 这个题最重要的是思路，感觉遍历一个数，然后使用hash去判断所需的另外一个数是否存在，机智的很啊

s = {1, 2, 3, 4}
sum = 5
s1 = set()

for i in s:
	n = sum - i
	if n in s:
		if (i, n) not in s1 and (n, i) not in s1:
			s1.add((i, n))

print s1
		

