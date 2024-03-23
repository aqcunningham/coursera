def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

# print('characters', len('fejiow, 78954jgeo jgeok!'))


# text= 'you do not need! this is joke!'

# words = text.split()
# word_count = {}
# for word in words:
#     word = word.strip(' .,!?').lower()
#     word_count[word] = word_count.get(word, 0) + 1
# wordscount = len(words)    
# print(wordscount)
# firstLetter = text[0]
# new = firstLetter.upper()
# print(text[0] == text[0].upper())
# print(text[-1] == '!')

# Given implementations of some string-related methods. 
# DO NOT CHANGE THIS FILE

def word_count(sentence):
    # Function to check the number of words. Returns the word count in string.
    words = len(sentence.split())
    # print(words)
    return words

def char_count(sentence):
    # Function to check the number of characters. Returns the character count in string.
    chars = len(sentence)
    # print(chars)
    return chars

def first_char(sentence):
    # Function to check the first character using the string index. Returns the first character in string.
    first = sentence[0]
    return first

def last_char(sentence):
    # Function to check the last character using the string index. Returns the last character in string.
    last = sentence[-1]
    return last


# from math import pi
# # print(math.pi)

# for x in range(1, 4):
#     print(int((str((float(x))))))

# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# for x in sample_dict:
#     print(x)

# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)

# recursion(11)

str = 'Pomodoro'
for l in str:
    if l == 'o':
        str = str.split()
        print(str, end=", ")