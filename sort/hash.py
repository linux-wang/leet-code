# coding:utf-8
# hash
# 实现hash算法，最简单的版本，长度为10，选取10以下最接近的一个质数做取余运算，此处为7
# 处理冲突的方法，采用拉链法

class HashObject(object):
	l = []
	def __init__(self):
		self.l = [[] for i in range(10)]

	def _hash(self, n):
		index = n % 7
		if n not in self.l[index]:
			self.l[index].append(n)
		else:
			pass
	
	def has(self, n):
		index = n % 7
		if n in self.l[index]:
			return True
		else:
			return False
	
	def get_hash(self):
		print self.l


if __name__ == '__main__':
	l = HashObject()
	l._hash(3)
	l._hash(3)
	l._hash(4)
	print l.has(3)
	print l.has(5)
	l.get_hash()

