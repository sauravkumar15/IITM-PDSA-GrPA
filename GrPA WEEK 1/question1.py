"""
Week 1 – Question 1 | PDSA (IIT Madras BS)

Problem Title:
--------------
Minimum Difference in P Elements

Problem Description:
--------------------
You are given a list of integers L and a positive integer P such that
the size of the list L is greater than P.

Write a function `find_Min_Difference(L, P)` that selects exactly P
different elements from the list such that the difference between
the maximum and minimum values among the selected elements is
minimum across all possible subsets of size P.

The function should return this minimum difference value.

Note:
-----
- There may be more than one subset of size P having the same minimum
  difference.
- Only the difference value needs to be returned.

Example:
--------
Input:
L = [3, 4, 1, 9, 56, 7, 9, 12, 13]
P = 5

Possible optimal subsets:
[3, 4, 7, 9, 9]
[7, 9, 9, 12, 13]

Minimum Difference:
9 - 3 = 6
13 - 7 = 6

Output:
6

Sample Input:
-------------
[3, 4, 1, 9, 56, 7, 9, 12]
5

Sample Output:
--------------
6
"""

def find_Min_Difference(arr, P):
    # Sort the array to bring close elements together
    arr.sort()
    n = len(arr)

    # Edge case handling
    if P == 0 or P > n:
        return 0

    min_diff = float('inf')

    # Sliding window of size P
    for i in range(n - P + 1):
        current_diff = arr[i + P - 1] - arr[i]
        min_diff = min(min_diff, current_diff)

    return min_diff


# Driver Code
if __name__ == "__main__":
    L = eval(input().strip())
    P = int(input())
    print(find_Min_Difference(L, P))
