#!/bin/python-
import os








#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    s = ''
    for i in sentence.split()(' '):
        s+=i[::-1] + ' '
    return s[-2::-1].swapcase()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    sentence = input()
    
    result = reverse_words_order_and_swap_cases(sentence)
    
    fptr.write(result + '\n')
    
    fptr.close()
    