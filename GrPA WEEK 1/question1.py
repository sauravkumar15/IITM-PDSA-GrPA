"""
Week 1 – Question 1 | PDSA (IIT Madras BS)

====================
QUESTION
====================
You are given a list of integers L and a positive integer P such that
the size of the list L is greater than P.

Write a function `find_Min_Difference(L, P)` that selects exactly P
different elements from the list such that the difference between
the maximum and minimum values among the selected elements is minimum.

Return this minimum difference value.

Note:
- Multiple subsets of size P may have the same minimum difference.
- Only the difference value should be returned.

Sample Input:
[3, 4, 1, 9, 56, 7, 9, 12]
5

Sample Output:
6
"""

# ====================
# SOLUTION
# ====================

def find_Min_Difference(arr, P):
    """
    Approach:
    ---------
    1. Sort the list.
    2. Use a sliding window of size P.
    3. For each window, compute (max - min).
    4. Return the minimum difference found.
    """

    arr.sort()
    n = len(arr)

    if P == 0 or P > n:
        return 0

    min_diff = float('inf')

    for i in range(n - P + 1):
        min_diff = min(min_diff, arr[i + P - 1] - arr[i])

    return min_diff


# ====================
# DRIVER CODE
# ====================
if __name__ == "__main__":
    L = eval(input().strip())
    P = int(input())
    print(find_Min_Difference(L, P))
