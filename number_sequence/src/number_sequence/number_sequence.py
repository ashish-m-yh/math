from functools import reduce
from operator import mul

import math


def lucas(n):
	s = [2,1,3]

	if n < 3:
		return s[n]

	i = s[-2]
	j = s[-1]

	count = 3

	while count <= n:
		j = j + i 
		count = count + 1
		j = i
		print (i, j)

	return i

def prime(n):
    for i in range(1, n//2, 2):
        print (i)
    return 

def fib(n):
	i = 0
	j = 1

	for i in (0, n):
		print (i, j)
		j = i + j


def sylvester_sequence(n):
    products = [2]
    for k in range(n):
        products.append(1 + reduce(mul, products, 1))

    return products

def tribonaci_sequence(n):
    if (n < 1):
        return
 
    tribs = []
    first = 0
    second = 0
    third = 1
 
    tribs.append(first)

    if (n > 1):
        tribs.append(second)

    if (n > 2):
        tribs.append(third)
 
    for i in range(3, n) :
        curr = first + second + third
        first = second
        second = third
        third = curr

        tribs.append(curr)

    return tribs

def is_pythagorean_triplet(x, y, z):
	sides = sorted([x,y,z])
	is_triplet = (sides[0]**2 + sides[1]**2) == sides[2]**2
	return is_triplet

def powers_of_x(x, n):
	powers = []

	for i in range(0, n+1):
		powers.append((x**i))

	return powers

def factorial(n):
	fact = 1

	for i in range(1, n+1):
		fact = fact * i

	return fact

def euler_numbers(n):
	return

def euler_zigzag(n):
	return

def fermat_numbers(n):
	fermat = []

	for i in range(0, n):
		p = 2**i
		f = 2**p + 1
		fermat.append(f)

	return fermat

def perfect_numbers(n):
	return

def jordan_polya_numbers(n):
	return

def semiprimes(n):
	return

def perrin_numbers(n):
	return

def cullen_numbers(n):
	return

def is_markov_triplet(x, y, z):
        total = x**2 + y**2 + z**2
        rhs = 3*x*y*z

        return (total == rhs)

def woodall_numbers(n):
	return

def semiperfect_numbers(n):
	return

def euclid_numbers(n):
	return

def is_kaprekar(n): 
    if n == 1:
        return True
      
    #Count number of digits in square
    sq_n = n * n
    count_digits = 1
    while not sq_n == 0:
        count_digits = count_digits + 1
        sq_n = sq_n // 10
      
    sq_n = n * n
    # Split the square at different points and see if sum
    # of any pair of splitted numbers is equal to n.

    r_digits = 0
    while r_digits < count_digits:
        r_digits = r_digits + 1
        eq_parts = (int) (math.pow(10, r_digits))
        if eq_parts == n:
            continue

        sum_digits = sq_n // eq_parts + sq_n % eq_parts
        if sum_digits == n:
            return True

    return False
     
def bernoulli_numbers(n):
	return

def star_numbers(n):
	stars = []

	for i in range(1, n+1):
		stars.append(6*i * (i-1) + 1)

	return stars

def triangular_numbers(n):
	nums = []

	for i in range(1, n+1):
		nums.append((i*(i+1))//2)

	return nums 

def padovan_sequence(n):
    # 0th ,1st and 2nd number of the series are 1
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1

    sequence = []

    for i in range(3, n+1):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext

        sequence.append(pNext)

    return sequence

def landau_function(n):
	return

def ramanujan_function(n):
	return

def palindromes(n):
	i = 0
	pals = []

	while n != len(pals):
		i = i + 1
		if str(i) == str(i)[::-1]:
			pals.append(i)
	
	return pals

def armstrong_numbers(n):
    armstrong = []

    for i in range(0, n):
        num = str(i)
        digits = map(int, num)

        total = 0
        for digit in digits:
            total = total + digit**len(num)

        if total == i:
            armstrong.append(i)

    return armstrong

import sys
#print(triangular_numbers(10))
print(sylvester_sequence(4))
print(is_kaprekar(13))
#print(padovan_sequence(7))
sys.exit()
print(is_markov_triplet(1,2,6))
print(tribonaci_sequence(20))
print(armstrong_numbers(10000))
print(factorial(5))
print(powers_of_x(2,5))
print(palindromes(100))
print(star_numbers(4))
print(fermat_numbers(15))
print(is_pythagorean_triplet(3,6,4))
