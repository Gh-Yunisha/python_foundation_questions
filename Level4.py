'''str1 = input("Enter any string:")
l = len(str1)
str2 = ''
for c in range(l-1, -1, -1):
    str2 = str2 + str1[c]
print("Reverse string:" + str2)'''
from typing import Dict, Any

'''str1 = input("Enter the string:")
val = str1
str2 = ''
l = len(str1)
for c in range(l-1, -1, -1):
    str2 = str2 + str1[c]
if val == str2:
    print("Palindrome")
else:
    print("Not palindrome")'''

'''str1 = input("Enter the string:")
l = len(str1)
count = 0
vowel = 'aeiouAEIOU'
for c in str1:
#for c in range(l):
    #x = str1[c].lower()
    #if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    if c in vowel:
        count += 1
print("Vowel count:", count)'''

'''str1 = input("Enter the string:").lower()
l = len(str1)
vc = 0
cc = 0
vowel = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
for c in str1:
#for c in range(l):
    #x = str1[c].lower()
    #if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    if c in vowel:
        vc += 1
    elif c in cons:
        cc += 1
print("Vowel count:", vc, "\tConsonant count:", cc)'''

'''str = input("Enter the string:")
freq = {}
for c in str:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print("Frequency of letters:", freq)'''

'''str1 = input("Enter any string:")
str2 = ''
sp = ' '
for c in str1:
    if c != ' ':
        str2 += c
print("Manipulated string:", str2)'''

'''str1 = input("Enter any string:")
str2 = ''
for c in str1:
    if c.islower():
        str2 += c.upper()
    elif c.isupper():
        str2 += c.lower()
print("Swap content:", str2)'''

'''str1 = input("Enter the string:")
str_list = list(map(str, str1.split()))
str2 = ''
longest = len(str_list[0])
for c in str_list:
    l1 = len(c)
    if l1 >= longest:
        longest = l1
        str2 = c

print(str2)'''

'''str1 = input("Enter string:")
str_list = list(map(str, str1.split()))
shortest = len(str_list[0])
str2 = ''
for c in str_list:
    l1 = len(c)
    if l1 <= shortest:
        shortest = l1
        str2 = c
print("Shortest words:", str2)'''

'''str1 = input("Enter string:")
str_list = list(map(str, str1.split(?)))
count = len(str_list)
print("Count:", count)'''

'''str = input("Enter a string:")
freq = {}
for c in str:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)
for k in freq:
    if freq[k] == 1:
        print("First non repeating character:", k)
        exit()'''

'''str = input("Enter a string:")
freq = {}
for c in str:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)
for k in freq:
    if freq[k] == 1:
        print("First non repeating character:", k)
        exit()'''

'''str = input("Enter the string:")
freq = {}
for c in str:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)
for k in freq:
    if freq[k] > 1:
        print("First repeating character:", k)
        exit()'''

'''str = input("Enter the string:")
freq = {}
str1 = ''
for c in str:
    if c in freq:
        freq[c] += 1
    else:
        str1 += c
        freq[c] = 1
print("Removing duplicate characters:", str1)'''

'''str1 = input("Enter the string:")
str2 = input("Enter the checking string:")
freq1 = {}
freq2 = {}
for c in str1:
    if c in freq1:
        freq1[c] += 1
    else:
        freq1[c] = 1
for k in str2:
    if k in freq2:
        freq2[k] += 1
    else:
        freq2[k] = 1
#freq1_sort = dict(sorted(freq1.items(), key=lambda item: item[1], reverse=True))
#freq2_sort = dict(sorted(freq2.items(), key=lambda item: item[1], reverse=True))

if freq1 == freq2:
    print("Anagram")
else:
    print("Not Anagram")'''

str1 = input("Enter the string:")
freq1 = {}
for c in str1:
    if c in freq1:
        freq1[c] += 1
    else:
        freq1[c] = 1
freq1_sort = dict(sorted(freq1.items(), key=lambda item:item[1], reverse=True))
print(freq1)
print(freq1_sort)
