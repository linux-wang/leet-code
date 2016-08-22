# -*- coding:utf-8 -*-
def abc_one(s):
    l = []
    s1 = s + ' '
    for i in s:
        for j in s:
            for k in s:
                if i != j and j != k and i != k:
                    l.append(i + j + k)
    return l


# 第二种是字典序排列，我能想到的只能是先排序再重复上面的过程
def abc_two(s):
    sort_s = sorted(s)
    abc_one(sort_s)


# 练习题2，求组合，数学公式
def abc_three(s):
    l = len(s)

    if l < 1:
        return False

    if l == 1:
        return 1

    x = 0
    for i in xrange(1, l + 1):
        m = reduce(lambda x, y: x * y, range(l + 1 - i, l + 1))
        n = reduce(lambda x, y: x * y, range(1, i + 1))
        x = x + m/n

    return x


if __name__ == '__main__':
    s = raw_input()
    print abc_three(s)
