def round_sum(a, b, c):
    nums = [a, b, c]
    new = []
    n = 0
    for i in nums:
        new.append(round10(i))
        n = n + 1
    return new[0] + new[1] + new[2]


def round10(num):
    if num % 10 <= 4:
        num_res = num - num % 10
 #       print('num1 = num - num % 10 ', num)
    else:
        num_res = num - num % 10 + 10
 #       print('num2 = num - num % 10 + 10 ', num)
    return num_res


print(round_sum(4, 12, 26))
print(round_sum(12, 5, 31))
print(round_sum(17, 23, 36))
print(round_sum(26, 12, 31))

print("abs= ",abs(4-5))
