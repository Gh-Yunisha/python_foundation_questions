'''41. Right Triangle Pattern
For n = 5:
*
**
***
****
*****
'''
for i in range(6):
    for j in range(i):
        print("*", end='')
    print()

'''42. Inverted Triangle 
***** 
**** 
*** 
** 
*
'''
for i in range(5, 1, -1):
    for j in range(i):
        print("*", end='')
    print()

'''43. Number Triangle 
1 
12 
123 
1234 
12345
'''
for i in range(1, 6, 1):
    for j in range(1, i+1):
        print(j, end='')
    print()

'''44. Repeated Number Triangle 
1 
22 
333 
4444 
55555
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end='')
    print()

'''45. Pyramid 
* 
*** 
***** 
******* 
*********
'''

n = 0
for i in range(4):
    for j in range(i):
        print((2*n-1)*"*")
        n += 1

'''46. Inverted Pyramid'''
n = 5
for i in range(4, 0, -1):
    for j in range(i):
        print((2*n-1)*"*")
        n -= 1

'''47. Floyd's Triangle 
1 
2 3 
4 5 6 
7 8 9 10
'''
n = 1
for i in range(5):
    for j in range(i):
        print(n, end=' ')
        n += 1
    print()

'''48. Pascal's Triangle'''
prev = [1]
for i in range(5):
    print(prev)
    new_row = [1]
    for j in range(len(prev) - 1):
        add = prev[j] + prev[j+1]
        new_row.append(add)

    new_row.append(1)
    prev = new_row



'''49. Multiplication Grid'''
header = ["*"]+[str(x) for x in range(1,11)]
print("\t".join(header))

for i in range(1,11):
    row = [str(i)]+[str(i*j) for j in range(1, 11)]
    print("\t".join(row))

'''50. Hollow Square 
For n = 5: 
***** 
*   * 
*   * 
*   * 
*****
'''
header = [str("*****")]
print("\t".join(header))
for i in range(1,4):
    for j in range(1,4):
        if j == 1 or j == 5:
            print("*   *" )
print("\t".join(header))