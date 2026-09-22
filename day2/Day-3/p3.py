'''
how to change one data type from another

'''

a=10
print(a)
print(type(a))

b="10"
#if we mention anything between two double course it will be treated as string
print(b)
print(type(b))

c=int(b)
#c=int("10")
print(c)
print(type(c))

d="7.8"
m=float(d)
t=int(m)
print(t)
print(type(t))

'''
if it a string contain float data type we cannot directly change it into int data type.
for the conversion we need to:

1.First we need to convert it into float
2.we need to convert it into int

'''
