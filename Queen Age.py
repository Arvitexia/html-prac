import numpy as np


def findQueenAge(arr):
    rows, cols = arr.shape
    r_idx = 0
    c_idx = 0

    # for min sum:
    # r_msum=float('inf')
    # c_msum=float('inf')

    # for r in range(rows):
    #     r_sum=0
    #     for c in range(cols):
    #         r_sum+=arr[r,c]
    #     if r_sum<r_msum:
    #         r_msum=r_sum
    #         r_idx=r

    # for c in range(cols):
    #     c_sum=0
    #     for r in range(rows):
    #         c_sum+=arr[r,c]
    #     if c_sum<c_msum:
    #         c_msum=c_sum
    #         c_idx=c

    # for max sum:
    r_msum = 0
    c_msum = 0

    for r in range(rows):
        r_sum = 0
        for c in range(cols):
            r_sum += arr[r, c]
        if r_sum > r_msum:
            r_msum = r_sum
            r_idx = r

    for c in range(cols):
        c_sum = 0
        for r in range(rows):
            c_sum += arr[r, c]
        if c_sum > c_msum:
            c_msum = c_sum
            c_idx = c

    age = arr[r_idx, c_idx]
    return age


# arr=np.array([[50,45,90,35],[70,80,60,95],[40,30,25,75]])
arr = np.array([[5, 3, 6], [7, 4, 9], [1, 2, 8]])
print(findQueenAge(arr))
