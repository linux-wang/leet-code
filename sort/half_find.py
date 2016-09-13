l = [2, 3, 4, 5, 7]
n = 7

def half_find(l, n, begin=0, end=len(l)-1):

	while(begin != end):
		mid = (begin + end) / 2
		if l[mid] == n:
			return mid
		if l[mid] < n:
			begin = mid + 1
		else:
			end = mid - 1
	return False
	

print half_find(l, n)
