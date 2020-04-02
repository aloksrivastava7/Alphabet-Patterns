'''
Enter Height : 10

**********
*
*
*
*
*
*
*
*
**********

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'*n)
        i = i + 1
    else :
        print('*')
