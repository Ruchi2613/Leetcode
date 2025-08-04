import sys


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        count = 0
        min_size = sys.maxsize


        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count+=1
            

            while r-l+1 == k:
                min_size = min(min_size, count)
                if blocks[l] == 'W':
                    count-=1
                l+=1

        return min_size

cl = Solution()
print(cl.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))