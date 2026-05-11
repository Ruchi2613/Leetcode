class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        
        d = {}

        for x in str(n):
            if int(x) in d:
                d[int(x)]+=1
            else:
                d[int(x)] = 1

        mini = sys.maxsize # type: ignore
        mini_el = 0
        
        for ele, freq in d.items():
            if mini > freq:
                mini = freq
                mini_el = ele
            elif mini == freq:
                mini_el = min(mini_el, ele)

        return mini_el
