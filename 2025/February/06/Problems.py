def equalFrequency(word: str):
    d = {}

    for x in word:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    # print(d)

    keys = []
    for key in d:
        keys.append(key)

    for ch in keys:
        d[ch] -= 1

        if d[ch] == 0:
            del d[ch]

        if len(set(d.values())) == 1:
            return True

        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return False

print(equalFrequency(word="abcc"))


'''3407. Substring Matching Pattern'''


def hasMatch(s: str, p: str) -> bool:
    i = -1

    for idx in range(len(p)):
        if p[idx] == '*':
            i = idx
            break

    if i == -1:
        return s == p

    p1, p2 = p[:i], p[i + 1:]

    j = -1

    for idx in range(len(s) - len(p1) + 1):
        print("p1",len(s) - len(p1) + 1)
        if s[idx:idx + len(p1)] == p1:
            j = idx
            break

    if j == -1:
        return False

    for idx in range(j + len(p1), len(s) - len(p2) + 1):
        print("p2",j + len(p1), len(s) - len(p2) + 1)
        if s[idx:idx + len(p2)] == p2:
            return True

    return False
print(hasMatch(s = "xks", p = "s*"))

'''1909. Remove One Element to Make the Array Strictly Increasing'''












