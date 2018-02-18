import os
import re
import matplotlib as plt

path = "DIR"

def find(path):
    for root, dirs, files in os.walk(path): # - --> is this correct to walk the root dir
        for f in files:
            count = re.search(r'{1,[0-9]}', f)   #count = re.search([\w]* ]
            return count
            print(count)
            plt.ylabel(count)
            plt.show()

# find(path)