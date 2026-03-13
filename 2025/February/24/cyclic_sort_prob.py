def dup_num(n):
    i = 0

    while i < len(n):
        c_i = n[i] - 1
        if n[i] != n[c_i]:
            n[i], n[c_i] = n[c_i], n[i]
        elif i != c_i:
            return n[i]
        else:
            i += 1


print(dup_num(n=[1, 3, 4, 2, 2]))


def findDuplicates(n):
    res = []
    i = 0

    while i < len(n):
        c_i = n[i] - 1
        if n[i] != n[c_i]:
            n[i], n[c_i] = n[c_i], n[i]
        elif i != c_i and n[i] not in res:
            res.append(n[i])
        else:
            i += 1

    return res

print(findDuplicates(n=[4,3,2,7,8,2,3,1]))
