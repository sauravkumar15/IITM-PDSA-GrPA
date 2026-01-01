@@ -0,0 +1,50 @@
"""
Week 1 – Question 3 | PDSA (IIT Madras BS)
====================
QUESTION
====================
Write a function named odd_one(L) that accepts a list L as argument. 
Except for one element, all other elements in L are of the same data type. 
The function odd_one should return the data type of this odd element.

Note:
(1) L has at least three elements.
(2) Elements will only be: int, float, str, bool.
(3) The function must return one of these strings: 'int', 'float', 'str', 'bool'.

Sample Input 1:
---------------
[1, 2, 3.4, 5, 10]

Sample Output 1:
----------------
float
"""

# ====================
# SOLUTION
# ====================

def odd_one(L):
    """
    Identifies the unique data type in a list where all other
    elements share a common data type.
    """
    # Create a list of type names as strings
    types = [type(x).__name__ for x in L]
    
    # Check the frequency of each unique type found
    # Since there's only one 'odd' type, its count will be 1
    for t in set(types):
        if types.count(t) == 1:
            return t

# ====================
# DRIVER CODE
# ====================

if __name__ == "__main__":
    # Use eval to convert the input string into a list object
    input_list = eval(input().strip())
    print(odd_one(input_list))
