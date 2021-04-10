"""
File: boggle.py
Name: Alice
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# This is the x, y direction which we need to check that 8 positions.
X = [-1, 0, 1, -1, 1, -1, 0, 1]
Y = [-1, -1, -1, 0, 0, 1, 1, 1]


def main():
	"""
	This is a program of boggle game. Users input 16 letters(4x4) and the program will print out the answers.
	"""
	line1 = input('1 row of letters: ')
	if check_form(line1) is False:
		print('Illegal input')
		return

	line2 = input('2 row of letters: ')
	if check_form(line2) is False:
		print('Illegal input')
		return

	line3 = input('3 row of letters: ')
	if check_form(line3) is False:
		print('Illegal input')
		return

	line4 = input('4 row of letters: ')
	if check_form(line4) is False:
		print('Illegal input')
		return

	line1_low_str = case_insensitive(line1)
	line2_low_str = case_insensitive(line2)
	line3_low_str = case_insensitive(line3)
	line4_low_str = case_insensitive(line4)

	lst_1 = []
	for ch in line1_low_str:
		lst_1.append(ch)
	lst_2 = []
	for ch in line2_low_str:
		lst_2.append(ch)
	lst_3 = []
	for ch in line3_low_str:
		lst_3.append(ch)
	lst_4 = []
	for ch in line4_low_str:
		lst_4.append(ch)

	# This is a dictionary recording the serial number and the letters which users input.
	d = {
		'00': lst_1[0], '10': lst_1[1], '20': lst_1[2], '30': lst_1[3],
		'01': lst_2[0], '11': lst_2[1], '21': lst_2[2], '31': lst_2[3],
		'02': lst_3[0], '12': lst_3[1], '22': lst_3[2], '32': lst_3[3],
		'03': lst_4[0], '13': lst_4[1], '23': lst_4[2], '33': lst_4[3]
		}
	book_lst = read_dictionary()
	x = 0
	y = 0
	ans_lst = []	 # the list to store the answers.

	# 16 times to go through all letter.
	for i in [0, 1, 2, 3]:
		for j in [0, 1, 2, 3]:
			boggle('', [], d, x+j, y+i, book_lst, ans_lst)
	print(f'There are {len(ans_lst)} words in total.')


def boggle(current_s, current_l, d, x, y, book_lst, ans_lst):
	if len(current_s) > 3:
		if current_s in book_lst:
			if current_s not in ans_lst:
				ans_lst.append(current_s)
				print(f'Found: {current_s}')
				if current_s in ans_lst:		# find out answers which are based on the current. e.g. room->roomy
					for i in range(8):
						if 4 > x + (X[i]) >= 0 and 4 > y + (Y[i]) >= 0:
							ch = str(x) + str(y)
							current_l.append(ch)
							current_s += str(d[ch])
							boggle(current_s, current_l, d, x + (X[i]), y + (Y[i]), book_lst, ans_lst)
							current_l.pop()
							current_s = current_s[:-1]

	else:
		if 4 > x >= 0 and 4 > y >= 0:
			ch = str(x) + str(y)		# Give a serial number t each letter
			if ch not in current_l:
				for i in range(8):
					if 4 > x+(X[i]) >= 0 and 4 > y+(Y[i]) >= 0:
						current_l.append(ch)
						current_s += str(d[ch])
						boggle(current_s, current_l, d, x+(X[i]), y+(Y[i]), book_lst, ans_lst)
						current_l.pop()
						current_s = current_s[:-1]


def check_form(s):
	if s[1].isspace() and s[3].isspace() and s[5].isspace():
		pass
	else:
		return False
	if s[0].isalpha() and s[2].isalpha() and s[4].isalpha() and s[6].isalpha():
		pass
	else:
		return False
	if len(s) == 7:
		pass
	else:
		return False
	return True


def case_insensitive(s):
	"""
	:param s: str, the four letters from users input.
	:return: str, the four letters in lower case.
	"""
	lower_str = ''
	for ch in s:
		if ch.isupper():
			lower_str += ch.lower()
		elif ch.islower():
			lower_str += ch
	return lower_str


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d_list = []
	with open(FILE, 'r')as f:
		for line in f:
			clean_line = line.strip()
			d_list.append(clean_line)
		return d_list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	book = read_dictionary()
	for i in range(len(book)):
		ele = book[i]
		word = str(ele)
		if word.startswith(sub_s):
			return True
		else:
			pass
	return False


if __name__ == '__main__':
	main()
