heights = sorted([int(input()) for _ in range(9)])

for hi in range(len(heights)):
    curr_height = sum(heights) - heights[hi]

    for hj in range(hi + 1, len(heights)):
        if curr_height - heights[hj] == 100:
            for hk, h in enumerate(heights):
                if hk != hi and hk != hj:
                    print(h)
            exit()
