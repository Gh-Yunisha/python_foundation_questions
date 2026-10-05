'''for i in range(6):
    for j in range(i):
        print("*", end='')
    print()'''

'''for i in range(5, 1, -1):
    for j in range(i):
        print("*", end='')
    print()'''

'''for i in range(1, 6, 1):
    for j in range(1, i+1):
        print(j, end='')
    print()'''

'''for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end='')
    print()'''
'''n = 0
for i in range(4):
    for j in range(i):
        print((2*n-1)*"*")
        n += 1'''

'''n = 5
for i in range(4, 0, -1):
    for j in range(i):
        print((2*n-1)*"*")
        n -= 1'''

'''n = 1
for i in range(5):
    for j in range(i):
        print(n, end=' ')
        n += 1
    print()'''


prev = [1]
for i in range(5):
    print(prev)
    new_row = [1]
    for j in range(len(prev) - 1):
        add = prev[j] + prev[j+1]
        new_row.append(add)

    new_row.append(1)
    prev = new_row



'''header = ["*"]+[str(x) for x in range(1,11)]

print("\t".join(header))
for i in range(1,11):
    row = [str(i)]+[str(i*j) for j in range(1, 11)]
    print("\t".join(row))'''

'''header = [str("*****")]
print("\t".join(header))
for i in range(1,4):
    for j in range(1,4):
        if j == 1 or j == 5:
            print("*   *" )
print("\t".join(header))'''



