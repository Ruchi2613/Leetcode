# 1.389. Find the Difference
#3.
def findTheDifference(s: str, t: str):
    d = {}

    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    print(d)

    for ch in t:
        if ch not in d or d[ch] == 0:
            return ch
        else:
            d[ch] -= 1

print(findTheDifference(s = "abcd", t = "abcdd"))



# 1.Possible Words using given characters in Python
def charCount(input,charSet):
    res = []
    for x in input:
        is_valid = True
        for y in x:
            if y not in charSet:
                is_valid = False
                break
        if is_valid:
            res.append(x)
    return ' '.join(res)



print(charCount(input = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run'],
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']))


#2.Python – Keys associated with Values in Dictionary


def reverse_dict(test_dict):
    res = {}

    for key,value in test_dict.items():
        for val in value:
            if val not in res:
                res[val] = [key]
            else:
                res[val].append(key)
    return res


print(reverse_dict(test_dict={'abc': [10, 30], 'bcd': [30, 40, 10]}))


