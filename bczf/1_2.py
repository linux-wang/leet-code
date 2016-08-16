# -*- coding:utf-8 -*-

# o(mn)
def is_contain_one(s1, s2):
	for c in s2:
		if c in s1:
			continue
		else:
			return False
	return True


# o(m) + o(n)
# 实际上和在编程珠玑里看到的位图排序很像，给一个位置，然后判断这个位置是否有值存在，原理一样
def is_contain_two(s1, s2):
	s = set()
	for c in s1:
		s.add(c)
	for c in s2:
		if s.__contains__(c):
			continue
		else:
			return False
	return True


# 还有第三种方法是：给每个字母一个质素，求第一个string的积，然后第二个一样，随后相除，判断是否有余数


if __name__ == '__main__':
	s1 = 'abc'
	s2 = 'bca'
	print is_contain_one(s1, s2)
	print is_contain_two(s1, s2)


# 变位词
# 兄弟单词：解决方式就是使用set，然后判断两个set是否相等
