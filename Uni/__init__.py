

#String

l = 'Hello'
print(l[::-1])
print(l[::-2])
print(l.upper())
print(l.lower())
print(l.__len__())
print(l[1])

print("--------------------------------")
#List of Tupls
l1 = [(1,3),(4,7),(5,2),(1,3),(4,7),(5,2)]

for (t1,t2) in l1:
    print(t1," ",t2)
print("--------------------------------")
for tup in l1:
    print(tup)
print("--------------------------------")
x=0
while x<5:
    print(l," ",x)
    x+=1
else: print("All Done")
print("--------------------------------")

for a in range(0,10):
    print(a)
print(type(a))

# for a1 in range(0,10):
#     print(a1)
print("--------------------------------")

l=[]
for leter in "word":
    l.append(leter)
print(l)
print("--------------------------------")
lst = [leter for leter in 'word']
print(lst)
print("--------------------------------")

celsius  = [10,20,21,25,30,35,40]
farengeit = [temp*9/5.0+32 for temp in celsius]
print(farengeit)

st = 'Proven ability to analyze existing systems and schedule upgrades to increase performance and productivity'
for word in st.split():
    if word[0] == 'a':
        print(word)
print("--------------------------------")

x = 25

def printer():
    x = 50
    return x
