# -*- coding:utf-8 -*-
# 我尼玛哭了，明明写的都一样，之前就不行，现在就行了
def partition(l, begin, end):
    p = l[begin]
    # import ipdb;ipdb.set_trace()
    while begin < end:
        while begin < end and l[end] >= p:
            end = end - 1
        l[begin] = l[end]

        while begin < end and l[begin] <= p:
            begin = begin + 1
        l[end] = l[begin]

    l[end] = p
    return begin 

 
def quick_sort(l=[], begin=0, end=0):
    if begin < end:
        p = partition(l, begin, end)
        quick_sort(l, begin, p-1)
        quick_sort(l, p+1, end)
    return l

l = [3, 2, 4, 5, 1] 
print quick_sort(l, 0, len(l)-1)
