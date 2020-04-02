'''

Enter Height : 15

*         *
*         *
*         *
*         *
*         *
*         *
***********
*         *
*         *
*         *
*         *
*         *
*         *
*         *
*         *s

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == n//2:
        print('*'*(3*(n//4)+2))
        i = i + 1
    else :
        print('*'+' '*(3*(n//4))+'*')
