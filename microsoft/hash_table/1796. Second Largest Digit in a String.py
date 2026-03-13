class Solution:
    def secondHighest(self, s: str) -> int:
        
        digit_num_set = set()

        for x in s:
            if x.isdigit():
                digit_num_set.add(int(x))

        if len(digit_num_set) <= 1:
            return -1

        max_num = max(digit_num_set)

        d = {}

        for num in digit_num_set:
            if num not in d and max_num!= num:
                d[num] = max_num - num

        min_val = min(d.values())
        # print(min_val)
        for k, v in d.items():
            if v == min_val:
                return k


        #2nd sol:

        # digit_num_set = set()

        # for x in s:
        #     if x.isdigit():
        #         digit_num_set.add(int(x))

        # if len(digit_num_set) <= 1:
        #     return -1

        # max_num = max(digit_num_set)
        # digit_num_set.remove(max_num)
        
        # return max(digit_num_set)