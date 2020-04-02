'''

Enter Height : 15

*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*******

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == n:
        print('*'*(n//2))
    else :
        print('*'+' '*((n//2)-2)+'*')
