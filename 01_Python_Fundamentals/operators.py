# Topic : Python Operators 

# Arithmetic Operators

a = int(input('enter value of a'))
b = int(input('enter value of b'))

print(a)
print(b)

print('The addition of', a, '+', b ,'=' , a+b)
print('The substraction of',a ,'-', b, '=', a-b)
print('The multiplication of',a,'*',b,'=',a*b)
print(a/b)              # Division 
print(a//b)             # Double Division 
print(a%b)              # Remainder
print(a**b)             # Exponent

# Precedence 
#(),**,*,/,//,%,+,-

exp = 1+4*3/2-2
print(exp)

# Q: Area of rectangle 

l=int(input('enter the length'))
b=int(input('enter the breadth'))    
area = l*b
print('Area of rectangle',area)

# Assignment Operator 

a = 100
print(a)

a=10
a += 5 # a = a+5
print(a)

x=10
x -= 10 #x= x-10
print(x)

i=2
i **= 3 
print(i)

# Comparision Operator 

a=5
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

a=10
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

# Logical Operator 

# and, or, not 
a=True
b=False 
c=True
d=False

print(a and b)
print(b and d)
print(a and c)

print(a or b)
print(b or d)
print(a or c)

print(not a)
print(not b)

# Identity Operator

a=10.0
b=10
print(a==b)
print(a is b)

print(id(a))
print(id(b))

i=20
j=20
print(i is j)

print(id(i))
print(id(j))

k=257
t=257
print(k is t)


print(id(k)) 
print(id(t))

# Membership Operator


x='natasha'
print('n' in x)
print('b' in x)
print('N' in x)

print('n' not in x)
print('b' not in x)
print('N' not in x)