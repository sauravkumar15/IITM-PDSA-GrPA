
"""
Week 2 – Question 3 | PDSA (IIT Madras BS)
====================
QUESTION
====================
Merge two sorted arrays (A and B) in place using a custom swap method. 
After merging, A and B must both remain sorted in ascending order.

Operations allowed: read A[i] and A.swap(indexA, B, indexB).
"""

# ====================
# SOLUTION
# ====================

def mergeInPlace(A, B):
    n, m = len(A), len(B)

    for i in range(n):
        # If element in A is larger than the smallest in B, they must swap
        if A[i] > B[0]:
            A.swap(i, B, 0)

            # Re-sort B to maintain the property that B[0] is the smallest
            first = B[0]
            k = 1
            while k < m and B[k] < first:
                B.swap(k-1, B, k)
                k += 1
