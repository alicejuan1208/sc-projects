"""
File: largest_digit.py
Name: Alice
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number we need to find the the biggest digit.
	:return: int, the biggest digit.
	"""
	ans = helper(n, 0)
	return ans


def helper(n, best):
	"""
	:param n: int, the number we need to find the the biggest digit.
	:param best: int, currently biggest digit.
	:return: int, the biggest digit.
	"""
	if n < 0:		# if the number is negative number, change it to positive.
		n = -n
	if n < 10:
		if best != 0:
			return best
		else:
			return n		# if the first input number is less than 10, return it directly.
	else:
		if best == 0:
			standard = n % 10
		else:
			standard = best
		next_value = n // 10
		second_last = next_value % 10
		if second_last < standard:
			best = standard
		else:
			best = second_last
		return helper(next_value, best)


if __name__ == '__main__':
	main()
