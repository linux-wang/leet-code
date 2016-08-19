def abc_one(s):
    for i in s:
        for j in s:
            for k in s:
                if i != j and j != k and i != k:
                    print i + j + k


if __name__ == '__main__':
    s = raw_input()
    abc_one(s)
