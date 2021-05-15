# this stupidly hard project is done
from unittest import TestCase 
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):

    byte_lst = book_to_words(book_url)
    max_len = 0
    for i in byte_lst:
        if max_len < len(i):
            max_len = len(i)

    for i in range(max_len):
        byte_lst = count_sort(byte_lst, i, max_len - 1)

    return byte_lst

def count_sort(arr, curr_i, max_idx):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(128)]

    for i in arr:
        if max_idx - curr_i < len(i):
            count[i[max_idx - curr_i]] += 1
        else:
            count[0] += 1

    for i in range(128):
        count[i] += count[i-1]
 
    for i in range(len(arr) -1, -1, -1):
        if max_idx - curr_i < len(arr[i]):
            output[count[arr[i][max_idx - curr_i]] - 1] = arr[i]
            count[arr[i][max_idx - curr_i]] -= 1            
        else:
            output[count[0] - 1] = arr[i]
            count[0] -= 1            

    return output

def test_book(link='https://www.gutenberg.org/files/84/84-0.txt', title = 'FRANKENSTEIN'):
    tc = TestCase()

    print('BEGIN SORTING *{}*'.format(title))

    copy_lst = sorted(book_to_words(link))
    r_sort_lst = radix_a_book(link)
    tc.assertEqual(r_sort_lst, copy_lst)

    print('END SORTING *{}*: CORRECTLY SORTED'.format(title)+'\n')

def main():
    print()
    test_book() # frankenstein
    test_book('https://www.gutenberg.org/files/2701/2701-0.txt', 'MOBY DICK') # moby dick
    test_book('https://www.gutenberg.org/files/345/345-0.txt', 'DRACULA') # dracula
    test_book('https://www.gutenberg.org/files/4300/4300-0.txt', 'ULYSSES') # ulysses
    print('ALL BOOKS CORRECTLY SORTED')
    print('hooray')


main()

