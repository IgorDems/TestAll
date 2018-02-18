## Print the sum of numbers in a string. Consecutive digits should be considered a whole number
## input = 'hkasvfgsdvk12kbdkshfvksd ,bh2mnhjf'
## output = 14 (12+2)
import re

str = "hkasvfgsdvk12kbdkshfvksd ,bh2mnhjf"
print("Sum by easy way =", sum(int(x) for x in re.findall(r'[0-9]+', str)))

print("-----------------2d solution---------------------------")

a = re.split('(\d+)', str)
s = 0

for i in range(len(a) - 1):
    try:
        s = s + int(a[i])
        print('TempSum = ', s)
    except:

        print("This is an error message! String may contain unconvertable to \"int\" elements ")

print('TotalSum = ', s)

my_File = open("text_file.txt","r")
# Read the file
read_File = my_File.read()
# Split the words
words = read_File.split()
# Using a set will only save the unique words
unique_words = set(words)
# You can then print the set as a whole or loop through the set etc
file = open("xxx.txt", 'w')
for word in unique_words:
    file.write(word + ", ")
    print(word)
my_File.close()
file.close()
