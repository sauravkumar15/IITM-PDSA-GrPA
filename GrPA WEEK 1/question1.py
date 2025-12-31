 
Week 1
 

L1.1: Introduction to Jupyter notebooks and Google Colab
Video

L1.2: Implementation of Python codes (Part 1)
Video

L1.3: Python recap - I
Video

L1.4: Python recap - II
Video

L1.6: Exception handling
Video

L1.5: Python recap - III
Video

L1.7: Classes and Objects
Video

L1.8: Implementation of Python codes (Part 2)
Video

L1.9: Timing our code
Video

L1.10: Implementation of Python codes (Part 3)
Video

L1.11: Why efficiency matters?
Video

L1.12: Implementation of Python codes (Part 4)
Video

PPA 1 - Not Graded
Programming Assignment

PPA 2 - Not Graded
Programming Assignment

GrPA 1
Programming Assignment

GrPA 2
Programming Assignment

GrPA 3
Programming Assignment

Practice assignment 1 - Not Graded
Assignment

Week 1 - Graded Assignment 1
Assignment


left_arrow

Overview

Question

Test Cases

Code

Solution
right_arrow
Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.
Note - The list can contain more than one subset of p elements that have the same minimum difference value.

Example

Let L = [3, 4, 1, 9, 56, 7, 9, 12, 13] and P = 5

If we see the following two subsets of 5 elements from L

[3, 4, 7, 9, 9] or [7, 9, 9, 12, 13]

Here, the difference between the maximum value and the minimum value in both subset is 9 - 3 = 6 or 13 - 7 = 6 which is minimum. So the output will be 6.

Sample Input

[3, 4, 1, 9, 56, 7, 9, 12]
5
Output

6



solution:

def find_Min_Difference(arr, P):
    arr.sort()
    n = len(arr)
    if P == 0 or P > n:
        return 0  # or handle invalid input
    min_diff = float('inf')
    for i in range(n - P + 1):
        diff = arr[i + P - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Example usage:
L = eval(input().strip())  # e.g., [3, 4, 1, 9, 56, 7, 9, 12]
P = int(input())           # e.g., 5
print(find_Min_Difference(L, P))

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
