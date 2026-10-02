'''num = int(input("Enter the number:"))
fac = 1
for i in range(1, num+1):
    fac = fac * i
print("Factorial:", fac)'''
import math

'''num = int(input("Enter the number:"))
fac = 1
if num<0:
    print("Invlaid")
    exit()
for i in range(1, num+1):
    fac = fac * i
print("Factorial:", fac)'''

'''num = int(input("Enter the number to create the fibonacci sequence:"))
a = 0
b = 1
print(a)
print(b)
for i in range(num-2):
    c = a + b
    a = b
    b = c
    print(c)
'''

'''num = int(input("Enter the number to find the fibonacci number:"))
a = 0
b = 1
for i in range(num-2):
    c = a + b
    a = b
    b = c
print(c)'''

'''num = input("Enter the number separated by space:")
num_list = list(map(int,num.split()))
search = int(input("Enter the digit to count:"))
c = 0
for i in num_list:
    if i == search:
        c += 1
if c == 0:
    print("Not found")
else:
    print("Number of digit occurance =", c)'''


'''num = int(input("Enter the number:"))
var = num
add = 0
while num != 0:
    rem = num % 10
    add = add * 10 + rem
    num = num // 10
if add == var:
    print("Palindrome")
else:
    print("Not palindrome")'''

'''num = int(input("Enter the number:"))
c = 0
for i in range(1, num+1):
    if num % i == 0:
        c += 1
if c == 2:
    print("Prime")
else:
    print("Not Prime")'''


'''num = int(input("Enter the number:"))
res = 0
for i in range(1, num+1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        res = res + i

print("Sum of prime number:", res)'''


'''num = int(input("Enter the number:"))
res = 0
for i in range(1, num+1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        res = res + 1

print("Number of prime numbers:", res)'''


''''num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
minimum = min(num1, num2)
for i in range(minimum, 1, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(f"GDC for {num1} and {num2}:", i)
        exit()'''

'''num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
maximum = max(num1, num2)
var = 0
for i in range(maximum, num1*num2+1):
    if i % num1 == 0 and i % num2 == 0:
        var = i
        break
print(f"LCM for {num1} and {num2}:", var)'''


'''a = int(input("Enter the number:"))
var = a
root = math.sqrt(a)
if root * root == var:
    print("Perfect square")
else:
    print("Not Perfect Square")'''


'''a = input("Enter the number:")
c = len(a)
a = int(a)
var = a
res = 0
while a != 0:
    rem = a % 10
    res = res + math.pow(rem,c)
    a = a // 10
if res == var:
    print("Armstrong number")
else:
    print("Not Armstrong number")'''


'''def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

a = int(input("Enter the number:"))
var = a
res = 0
while a != 0:
    rem = a % 10
    res = res + fact(rem)
    a = a // 10
if res == var:
    print("Strong number")
else:
    print("Not Strong number")'''


'''a = input("Enter the number:")
c = len(a)
a = int(a)
root = int(math.pow(a,2))
if root % (10**c) == a:
    print("Automorphic number")
else:
    print("Not Automorphic number")'''

'''def prime_factors(n):
    num_list1 = []
    div = 2
    while n > 1:
        if n % div == 0:
            num_list1.append(div)
            n = n // div
        else:
            div += 1
    print("Prime factors:", num_list1)

prime_factors(14)
prime_factors(60)'''

'''def d2b(num):
    b = ''
    while num > 0:
        rem = num % 2
        b = str(rem) + b
        num = num // 2

    print("Binary number:", b)
d2b(4)'''
'''
num = int(input("Enter binary number:"))
d = 0
c = 0
while num > 0:
    rem = num % 10
    d = rem*pow(2,c) + d
    num = num // 10
    c +=1
print("decimal number:", d)'''
def d2n(num, base):
    b = ''
    while num > 0:
        rem = num % base
        b = hex_digit[rem] + b
        num = num // base
    print("Conversion number:", b)


var = int(input("Enter the decimal number:"))
base = int(input("Enter the base to convert to:"))
hex_digit = "0123456789ABCDEF"
d2n(var, base)

