
"""
Week 2 – Question 1 | PDSA (IIT Madras BS)
====================
QUESTION
====================
Write a Python function combinationSort(strList) that takes a list of unique 
strings strList as an argument, where each string is a combination of a 
letter from 'a' to 'z' and a number from 0 to 99. The initial character in 
the string is the letter (e.g., 'a23', 'd5', 'q99').

The function should return two lists (L1, L2):

L1: All strings sorted in ascending order with respect to the first 
    character only. Strings with the same initial character must remain 
    in the same order as in the original list (Stable Sort).

L2: Based on L1, sort strings starting with the same character in 
    descending order with respect to the number formed by the 
    remaining characters.

Sample Input 1:
---------------
d34, g54, d12, b87, g1, c65, g40, g5, d77

Sample Output 1:
----------------
L1: b87, c65, d34, d12, d77, g54, g1, g40, g5
L2: b87, c65, d77, d34, d12, g54, g40, g5, g1
"""

# ====================
# SOLUTION
# ====================

def combinationSort(strList):
    # L1: Stable sort based on the first character (letter)
    # Python's sorted() is stable by default
    L1 = sorted(strList, key=lambda x: x[0])
    
    # L2: Tiered sort based on the L1 results
    L2 = []
    i = 0
    n = len(L1)
    
    while i < n:
        char_group = L1[i][0]
        temp_group = []
        
        # Group elements that share the same initial character
        while i < n and L1[i][0] == char_group:
            temp_group.append(L1[i])
            i += 1
            
        # Sort the subgroup by numerical value in descending order
        # x[1:] extracts the numeric portion after the first letter
        temp_group.sort(key=lambda x: int(x[1:]), reverse=True)
        L2.extend(temp_group)
    
    return L1, L2

# ====================
# DRIVER CODE
# ====================

if __name__ == "__main__":
    # Split input by comma and space as per sample format
    strList = input().split(", ")
    L1, L2 = combinationSort(strList)
    
    print("L1:", ", ".join(L1))
    print("L2:", ", ".join(L2))
