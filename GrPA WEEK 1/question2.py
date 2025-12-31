"""
Week 1 – Question 2 | PDSA (IIT Madras BS)

====================
QUESTION
====================
Goldbach's Conjecture is one of the oldest unsolved problems in
number theory. It states that every even number greater than 2
can be expressed as the sum of two prime numbers.

Write a function `Goldbach(n)` where `n` is a positive even number
(n > 2) that returns a list of tuples (a, b) such that:
- a ≤ b
- a and b are prime numbers
- a + b = n

Sample Input 1:
---------------
12

Sample Output 1:
----------------
[(5, 7)]

Sample Input 2:
---------------
26

Sample Output 2:
----------------
[(3, 23), (7, 19), (13, 13)]
"""

# ====================
# SOLUTION
# ====================

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def Goldbach(n):
    """
    Returns a list of tuples (a, b) such that:
    - a and b are prime
    - a + b = n
    - a <= b
    """
    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append((i, n - i))
    return result


# ====================
# DRIVER CODE
# ====================
if __name__ == "__main__":
    n = int(input())
    print(sorted(Goldbach(n)))
