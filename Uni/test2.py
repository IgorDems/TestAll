str = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
res = ""
# str = str.replace("X","")
#
# print(str)

i=0
for i in range(len(str)):
    if str[i] != "X":
        res = res + str[i];
        i = i + 1;
    else :
        i = i + 1
print(res)

