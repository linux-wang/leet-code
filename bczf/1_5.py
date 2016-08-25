# -*- coding:utf-8 -*-

def huiwen(s):
    if not s:
        return False
    return s == s[::-1]

def long_huiwen(s):
    max_len = 0
    m = n = 0

    if len(s) == 1:
        return 1

    if not len(s):
        return False

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            ss = s[i:j+1]
            if huiwen(ss) and j+1-i > max_len:
                max_len = j + 1 -i
                m = i
                n = j
    return max_len

if __name__ == '__main__':
    print long_huiwen('1')
