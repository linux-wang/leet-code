def abc_one(s):
    for i in s:
        for j in s:
            for k in s:
                if i != j and j != k and i != k:
                    print i + j + k


# 第二种是字典序排列，我能想到的只能是先排序再重复上面的过程
def abc_two(s):
    sort_s = sorted(s)
    abc_one(sort_s)


if __name__ == '__main__':
    s = raw_input()
    abc_one(s)
