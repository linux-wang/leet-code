import copy

def left_shift_one(l, n):
	for i in range(n):
		t = l[0]	
		for j in range(len(l)-1):
			l[j] = l[j+1]
		l[-1] = t
	print l

def left_shift_two(l, n):
	l1 = l[:n]
	l1.reverse()
	l2 = l[n:]
	l2.reverse()

	l = l1 + l2
	l.reverse()
	print l


# exercise
def reverse_sentence(s):
	l = s.split()
	l.reverse()
	print ' '.join(l)


if __name__ == '__main__':
	l = [1, 2, 3, 4, 5]
	l1 = copy.deepcopy(l)
	n = 3

	left_shift_one(l, n)
	left_shift_two(l1, n)
	
	s = 'I am a student.'
	reverse_sentence(s)
