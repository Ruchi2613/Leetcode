class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    # stack = [-1]
    # max_area = 0
    # for i in range(len(heights)):
    #     print("   ", stack)
    #     while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
    #         current_height = heights[stack.pop()]
    #         current_width = i - stack[-1] - 1
    #         max_area = max(max_area, current_height * current_width)
    #         print(i, current_height,  current_width, max_area)
    #     stack.append(i)

    # print(stack)
    # print(max_area)

    # while stack[-1] != -1:
    #     current_height = heights[stack.pop()]
    #     current_width = len(heights) - stack[-1] - 1
    #     max_area = max(max_area, current_height * current_width)
    # return max_area
    def largestRectangleArea(self, arr: List[int]) -> int:

        stk1, stk2 = [], []
        n = len(arr)
        lt, rt = [-1] * n, [n] * n
        # Finding nearest smaller to left
        for i in range(n):
            while stk1 and stk1[-1][0] >= arr[i]:
                stk1.pop()

            if stk1:
                lt[i] = stk1[-1][1]
            stk1.append((arr[i], i))

        # Finding nearest smaller to right
        for i in range(n - 1, -1, -1):
            while stk2 and stk2[-1][0] >= arr[i]:
                stk2.pop()

            if stk2:
                rt[i] = stk2[-1][1]
            stk2.append((arr[i], i))

        # Calculating maximum area
        max_area = 0
        for i in range(n):
            width = rt[i] - lt[i] - 1
            area = width * arr[i]
            max_area = max(max_area, area)

        return max_area
