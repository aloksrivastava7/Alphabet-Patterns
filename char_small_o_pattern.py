'''

Enter Height : 10

******
*    *
*********
*    *
*    *
*    *
*    *
*    *
*    *
******

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'*(3*(n//4)))
        i = i + 1
    elif i == n//3:
        print('*'*(n-1))
        i = i + 1
    else :
        print('*'+' '*(3*(n//4)-2)+'*')

