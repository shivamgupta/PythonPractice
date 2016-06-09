"""
Description: Python script to identify if a given number is a happy number or not.
Source: Happy Number Wiki: https://en.wikipedia.org/wiki/Happy_number
Author: Shivam Gupta (shivamvmc@gmail.com)
"""

def get_digits(n):
	"""
	Returns an array with all the digits in a number

	Example: 19 -> [1, 9]
	"""
	number_of_digits = len(str(n))
	digits = []

	for i in str(n):
		digits.append(i)
	
	return digits

def get_squares_sum(n):
	"""
	Returns a squared sum of all the digits in the given number n

	Example: 19 -> 82
	"""
	n_digits = get_digits(n)
	sq_sum = 0.0
	
	for i in n_digits:
		sq_sum = sq_sum + (int(i)*int(i))

	return int(sq_sum)

def if_happy(n):
	"""
	Python script to identify if a given number is a happy number or not.

	Example: 19 -> "A Happy Number"
			 20 -> "Not a Happy Number"
	"""
	sq_sum = get_squares_sum(n)
	i = 0

	while sq_sum != 1:
		sq_sum = get_squares_sum(sq_sum)

		i = i + 1
		
		if i > 10000:
			return "Not a Happy Number"

	if sq_sum == 1:
		return "A Happy Number"
