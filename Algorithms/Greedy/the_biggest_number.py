# Given a string(S), using + or * between each char, return the biggest output

# Idea
# set result to first elem, iter from index 1

# my answer
def fun(s):
    # try1
    # elems = list(s)
    # result = int(elems[0])
    # for i in elems:
    #     if int(i) == 0:
    #         pass
    #     elif int(i) > 0:
    #         result *= int(i)
    # return result

    # try2
    result = int(s[0])
    for i in range(1, len(s)):
        elem = int(s[i])
        if elem <= 1 or result <= 1:
            result += elem
        else:
            result *= elem
    return result


# ex answer
def fun2(s):
    result = int(s[0])
    for i in range(1, len(s)):
        num = int(s[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result


print(fun('02984'))
print(fun2('02984'))
