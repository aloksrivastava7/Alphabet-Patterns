'''
Enter Height : 15

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*********

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == n:
        print('*'*(3*(n//4)))
        i = i + 1
    else :
        print('*')
