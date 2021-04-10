"""
File: anagram.py
Name: Alice
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
d_list = []     # the list of dictionary data
ans = []    # the list to show the answer of anagram


def main():
    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    while True:
        target = input('Find anagrams for: ')
        global ans
        ans = []
        if target == '-1':
            break
        else:
            find_anagrams(target)


def read_dictionary():
    with open(FILE, 'r')as f:
        for line in f:
            clean_line = line.strip()
            d_list.append(clean_line)
        return d_list


def find_anagrams(s):
    """
    :param s: string, the word that users input to find anagrams.
    """
    book = read_dictionary()
    lst = []
    for ch in s:
        lst.append(ch)
    print('Searching...')
    find_anagrams_helper(s, lst, [], '', book)
    num = len(ans)
    print(f'{num} anagrams: {ans}')


def find_anagrams_helper(s, lst, current, current_s, book):
    """
    :param s: string, the word that users input to find anagrams.
    :param lst: list, change the s to the list data type.
    :param current: list, An Empty list to save the current data.
    :param current_s: string, An Empty string to save the current data.
    :param book: list, the data of dictionary.txt
    """
    if len(current) == len(lst) and len(current_s) == len(s):
        if current_s in book:
            global ans
            if current_s not in ans:
                ans.append(current_s)
                print(f'Found: {current_s}')
                print('Searching...')

    else:
        for i in range(len(lst)):
            lst[i] = i
            if lst[i] not in current:
                current.append(lst[i])
                current_s += s[i]
                find_anagrams_helper(s, lst, current, current_s, book)
                current.pop()
                current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: the string of current combination.
    :return: bool, if sub_s is contained in the word of dictionary.
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
