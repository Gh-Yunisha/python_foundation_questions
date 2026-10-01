#1. Even or Odd
n=int(input("Enter any number:"))
if n%2==0:
    print("Even")
else:
   print("Odd")

#2.Positive, negative or zero
num = int(input("Enter number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#3. Largest of two
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
if num1>num2:
    print(num1," is greatest")
else:
    print(num2, " is greatest")

#4. Largest of three
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
if num1>=num2 and num1>=num3:
    print(num1, " is greatest")
elif num2>=num1 and num2>=num3:
    print(num2," is greatest")
else:
    print(num3," is greatest")

#5. Divisible by both 3 and 5
num = int(input("Enter:"))
if num%3==0 and num%5==0:
    print(num," in divisible by both 5 and 3.")
else:
    print("Not")

#6. Leap year
year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")

#7. Grade Calculator
grade = input("Enter your grade:").upper()
if grade == 'A':
    print("Excellent! Your grade is", grade)
elif grade == 'B':
    print("Good! Your grade is", grade)
elif grade == 'C':
    print("Great! Your grade is", grade)
elif grade == 'D':
    print("You can do better! You got", grade)
elif grade == 'F':
    print("Work Harder! Your grade is", grade)
else:
    print("Invalid")

#8.Simple calculator
a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
op = input("Enter operator:")
if op == '+':
    res= a+b
    print(res)
elif op == '-':
    res = a-b
    print(res)
elif op == '*':
    res = a*b
    print(res)
elif op == '/':
    try:
        res = a/b
        print(res)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print()
elif op == '%':
    res = a%b
    print(res)
else:
    res = "Invalid"
    print(res)

#9. Absolute value
num = int(input("Enter the number:"))
if num<0:
    num = -num
else:
    num = num
print(num)

#10. Number of digits
num = int(input("Enter the number:"))
c = 0
if num == 0:
    print("Number of digit = 1")
    exit()
while num!=0:
    c = c+1
    num=int(num/10)
print("Number of digit =", c)

#11. Sum of Digits
num = int(input("Enter the number:"))
sum = 0
while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10
print("Sum of digit =", sum)

#12. Product of digits
num = int(input("Enter the number:"))
prod = 1
if num == 0:
    prod = 0
while num != 0:
    rem = num % 10
    prod = prod * rem
    num = num // 10

print("Product of digit =", prod)

#13. Reverse a number
num = int(input("Enter the number:"))
sum = 0
while num != 0:
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10

print("Reverse of digit =", sum)

#14. First and last digit
num = int(input("Enter the number:"))
lastdigit = num % 10
firstdigit = 0
rem = 0
while num != 0:
    rem = num % 10
    num = num // 10

firstdigit = rem
print("First Digit =", firstdigit, "Last Digit =", lastdigit)

#15. Multiplication Table
num = int(input("Enter the number to find the multiplication table:"))
for i in range(1,11):
    print(num, "x", i, "=", num*i)

#16. Sum of 1 to N
num = int(input("Enter the number:"))
res = 0
for i in range(1, num+1):
    res = res + i
print("Sum =", res)

#17. Sum of Even Numbers
num = int(input("Enter the number:"))
res = 0
for i in range(2, num+1, 2):
    res = res + i
print("Sum =", res)

#18. Count even and odd
ch = 'Y'
even_count = 0
odd_count = 0
while ch == 'Y':
    num = int(input("Enter the number:"))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    ch = input("Want to continue?(y/n):").upper()
print("Even =", even_count, "Odd =", odd_count)

#19. Find the largest
num = input("Enter the number:")
num_list = list(map(int,num.split()))
largest = num_list[0]
for i in range(len(num_list)):
        if num_list[i] > largest:
            largest = num_list[i]

print("Largest =", largest)

#20. Find the smallest
num = input("Enter the number:")
num_list = list(map(int,num.split()))
smallest = num_list[0]
for i in num_list:
        if i < smallest:
            smallest = i

print("Smallest =", smallest)


