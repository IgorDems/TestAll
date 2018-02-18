# Python 2 and 3: option 2
from functools import reduce


def double_char(str):
    res = ''
    for i in str:
        res = res + i * 2
    return  print(res)


double_char('sdjfhjkslryewl')

str = 'How long are the words in this phrase'


def word_len(str):
    res = list(map(len, str.split()))
    return print(res)


word_len(str)

print("----------------- next 1------------------------")


def digits_to_num(digits):
    return reduce(lambda x, y: x * 10 + y, digits)


print(digits_to_num([3, 4, 3, 2, 1, 3, 2]))
print("----------------- next 2------------------------")


def filter_words(word_list, letter):
    return filter(lambda word: word[0] == letter, word_list)


l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
r = filter_words(l, 'h')
print(r, l)
print("----------------- next 3------------------------")


def concatenate(L1, L2, connector):
    return [word1 + connector + word2 for (word1, word2) in zip(L1, L2)]


print(concatenate(['A', 'B'], ['a', 'b'], '-'))
print("----------------- next 4------------------------")


def count_match_index(L):
    return len([num for count, num in enumerate(L) if num == count])


print(count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))


def d_list(L):
    return {key: value for value, key in enumerate(L)}


print(d_list(['a', 'b', 'c']))

print(globals())
print(locals())
