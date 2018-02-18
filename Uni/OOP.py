x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
print("----------------------------------------")
name = 'This is a global name'


def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello ' + name)
    hello()
greet()

print("----------------------------------------")
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
print("----------------------------------------")
def check_rang(num, min, max):
    if num in range(min, max+1):
        print('%s inside range'%str(num))
    else:
        print("Out")
check_rang(3,1,10)
print("----------------------------------------")
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
print("----------------------------------------")
def unique_list(l):
    # Also possible to use list(set())
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return print(x)

l=['a','s','d','f','s','d','a','s','','d','s']
unique_list(l)
print("----------------------------------------")

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphabet)
    print(alphaset)
    return print(alphaset <= set(str1.lower()))

ispangram("The quick brown fox jumps over the lazy dog")
string.ascii_lowercase
print(string.ascii_lowercase)



print("----------------------------------------")


def palindrome(s):
    s = s.replace(' ','')  # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]  # Check through slicing

print("----------------------------------------")
print("----------------------------------------")
