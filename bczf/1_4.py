# -*- coding: utf-8 -*-

def palindrome_one(s):
    return s == s[::-1]

# 妈蛋觉得这样写根本锻炼不到什么能力，orz，要果断回去用cpp写么…
# 觉得这个效率实际上已经很高了 o(n)
def palindrome_two(s):
    if not s:
        return True

    start = 0
    end = len(s) - 1

    while(start != end):
        if s[start] == s[end]:
            start = start + 1
            end = end - 1
            continue
        return False
    return True


if __name__ == '__main__':
    s = raw_input('input a string: ')
    print palindrome_one(s)
    print palindrome_two(s)
