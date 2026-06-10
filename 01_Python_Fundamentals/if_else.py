# Topic: Conditional Statements 

# IF ELSE Statement 

# Q Positive and Negative number
n = int(input('enter n'))
if n > 0:
    print(n,'is positive')
else: 
    print(n,'is negative')

# Q Odd or Even number 
n = int(input('enter n'))
if n%2 ==0:
    print(n,'is even')
else: 
    print(n,'is odd') 

# Multiple Conditions 

# Q taking 3 inputs , 2 numbers and one operator (+,-,*).
a = int(input('enter a'))
b = int(input('enter b'))
c = input('enter operator')

if c == '+':
    print(a+b) 
elif c == '-':
    print(a-b)
elif c == '*': 
    print(a*b)
else:
    print('Invalid')

# Q Take marks as input and grade the marks 
m = int(input('enter marks'))

if m>90 and m<=100:
    print('A')
elif m>70 and m<=90:
    print('B')
elif m>50 and m<=70:
    print('C')
elif m>30 and m<=50:
    print('D')
else:
    print('E')
    
# Q Take salary as input and put tax percent then calculate net salary.
sal = int(input('enter salary'))
if sal < 25000:
    print('net salary', sal - (sal*0)/100)
elif sal >= 25000 and sal < 50000: 
    print('net salary', sal - (sal*10)/100) 
elif sal >= 50000 and sal < 100000: 
    print('net salary', sal - (sal*30)/100) 
else: 
    print('net salary',sal - (sal*50)/100) 

# Q Take number input and check if no.is divisible by 5,7 both ,only by 5 ,only by 7 or by none of them 
n = int(input('enter n'))

if n%5 == 0 and n%7 == 0:
    print(n,'is divisible by 5 and 7 both')
elif n%5 == 0:
    print(n,'is divisible by only 5')
elif n%7 == 0: 
    print(n,'is divisible by only 7') 
else: 
    print(n,'is not divisible by none of them')

# Nested Queries 

# Q Take number input and check if no.is divisible by 5,7 both ,only by 5 ,only by 7 or by none of them 
n = int(input('enter n'))

if n%5 == 0:
    if n%7 == 0:
        print(n,'is divisible by both 5 ,7')
    else:
        print(n,'is divisible by 5 only')
elif n%7 == 0:
    print(n,'is divisible by 7 only')
    
else: 
    print(n,'is not divisible by any of them') 

# Q Take input of weather . sunny ,winter,rainy also thier temp and con and then print play or not play 
w = input('enter weather')

if w == 'sunny':
    temp = int(input('enter temp'))
    if temp >= 30 and temp <= 50:
        print('play') 
    else: 
        print('not play') 
        
elif w == 'winter': 
    temp = int(input('enter temp'))
    if temp >= 10 and temp <= 20:
        print('play') 
    else:
        print('not play')
    
elif w == 'rainy':
      con = input('enter rainy con')
      if con == 'heavy':
          print('not play') 
      else:
          print('play')
else:
    print('Invalid') 

# Q Restaurent menu
print('Available Items are Pizza Burger')
order = input('place your order:')
if order == 'Pizza':
    top = input('select toppings veggies, corn, cheese')
    if top == 'veggies':
        print('your',top,order,'price is 150')
    elif top == 'corn':
        print('your',top,order,'price is 180')
    elif top == 'cheese':
        print('your',top,order,'price is 220')
    else:
        print(top,order,'is not available')
elif order == 'Burger':
    category = input('select category veg, non veg')
    if category == 'veg':
        print('Your',category,order,'price is 60')
    else : 
        print('your',category,order,'price is 300')
else:
    print('Your order is not on the menu')

