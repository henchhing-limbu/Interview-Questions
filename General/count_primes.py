"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

# Intuitively, we would go from 1 all the way to n and check if each number
# is prime number or not. We keep track of total number of prime nubers.
# To check if a number is prime or not, we can check if it's divisble by any
# number less than or equal to square root of that number. You can just google
# the proof of this fact.

# To check if a number is prime, it takes O(N^0.5).
# We check if a number is prime for N numbers.
# So, time complexity becomes O(N.N^0.5) = O(N^1.5).
# Space complexity is constant time O(1) because we are not using any extra
# space.

import math

def is_prime(num):
    if num == 2:
        return True
    # math.ceil returns float in python2.
    for x in range(2, int(math.ceil(math.sqrt(num))) + 1):
        if num % x == 0:
            return False
    return True

def count_primes(n):
    num_of_prime_nums = 0
    for num in range(2, n):
        if is_prime(num):
            num_of_prime_nums += 1
    return num_of_prime_nums

assert count_primes(10) is 4
assert count_primes(3) is 1 
assert count_primes(100) is 25


# This can be further optimized using the idea of Sieve of Eratosthenes.
# Instead of looking if each number is prime number or not, we identify
# numbers that are not prime.
# You can check the hint section in description tab to know more on this
# algorithm. Since, we do not call is_prime() method for each num, the
# time complexity drops to O(nloglogn).
# Note: the time complexity of harmonic series is O(logn).
# These links might be helpeful to understand Big-O of this Sieve of
# Eratosthenes.
# https://medium.com/@chenfelix/time-complexity-sieve-of-eratosthenes-fb0184da81dc
# https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm
# Space complexity would be O(n) as we are using list of size n.

def count_primes_optimized(n):
    num_of_primes = 0
    prime_nums = [True]*(n+1)
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if prime_nums[i]:
            j = i**2
            while j < n:
                prime_nums[j] = False
                j += i
    for i in range(2, n):
        if prime_nums[i]:
            num_of_primes += 1
    return num_of_primes

assert count_primes_optimized(10) is 4
assert count_primes_optimized(3) is 1
assert count_primes_optimized(100) is 25

