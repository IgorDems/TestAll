# For using the same code in either Python 2 or 3
from __future__ import print_function

## Note: Python 2 users, use raw_input() to get player input. Python 3 users, use input()

def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')

            continue
        else:
            break

    print('Thank you, you number squared is: ', n ** 2)


ask()
