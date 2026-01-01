
"""
Week 2 – Question 2 | PDSA (IIT Madras BS)
====================
QUESTION
====================
Find the largest number in a list L of unique numbers that are 
sorted (ascending) and rotated n times.

Constraint: Must be O(log n) solution. Do not use list slicing.

Sample Input: 7, 8, 2, 4, 5
Sample Output: 8
"""

# ====================
# SOLUTION
# ====================

def findLargest(L):
    """
    Uses binary search to find the maximum element in a rotated sorted list.
    """
    left, right = 0, len(L) - 1
    
    # If the list is not rotated at all
    if L[left] <= L[right]:
        return L[right]
    
    while left <= right:
        mid = (left + right) // 2
        
        # If mid is the largest: L[mid] > L[mid + 1]
        if mid < len(L) - 1 and L[mid] > L[mid + 1]:
            return L[mid]
            
        # If mid is the smallest: L[mid] < L[mid - 1]
        if mid > 0 and L[mid] < L[mid - 1]:
            return L[mid - 1]
            
        # Decide which direction to search
        if L[mid] >= L[left]:
            # Left side is sorted, largest must be on the right
            left = mid + 1
        else:
            # Right side is sorted, largest must be on the left
            right = mid - 1
            
    return L[left]
