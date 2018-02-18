def wish(message):
    return lambda name: message.upper() + name


greet = wish("Ha Bi")
greet("Jon")
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)


def welcome(name):
    return "Welcom " + name, "Good Bye" + name


wish = welcome("Joe")
print(wish)
print(30 // 7)

for i in range(3):
    print(i)
