# -*- coding:utf-8 -*-
 
def buble_sort(l):
    for i in range(len(l)-1):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                t = l[i]
                l[i] = l[j]
                l[j] = t

    return l

print buble_sort([3, 2, 1, 1, 4])

