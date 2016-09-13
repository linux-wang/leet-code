l = [1, 3, 4, 9, 8, 6]
n = 5

def order_find(l, n):
	for i in l:
		if i == n:
			return l.index(i)
	if i == len(l):
		return False

print order_find(l, n)
	
