import sys


def minWindow(s: str, t: str) -> str:
    # Create a dictionary for t using basic loops
    t_count = {}
    for char in t:
        if char in t_count:
            t_count[char] += 1
        else:
            t_count[char] = 1

    # Initialize variables
    s_count = {}
    i = 0
    j = 0
    min_len = sys.maxsize
    min_start = 0
    matched_chars = 0

    # Traverse the string s
    while j < len(s):
        char = s[j]
        if char in s_count:
            s_count[char] += 1
        else:
            s_count[char] = 1

        # Check if the current character satisfies t's requirement
        if char in t_count and s_count[char] == t_count[char]:
            matched_chars += 1

        # Shrink the window
        while matched_chars == len(t_count):
            # Update the minimum window
            if (j - i + 1) < min_len:
                min_len = j - i + 1
                min_start = i

            # Shrink from the left
            left_char = s[i]
            s_count[left_char] -= 1
            if left_char in t_count and s_count[left_char] < t_count[left_char]:
                matched_chars -= 1

            i += 1

        j += 1

    # Return the result
    if min_len > len(s):
        return ""
    return s[min_start:min_start + min_len]


print(minWindow(s='aabc', t='abc'))
