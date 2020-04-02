'''

Enter Height : 15

***************
*
*
*
*
*
*      *******
*              *
*              *
*              *
*              *
*              *
*              *
*              *
***************

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'*n)
    elif i == (n//2):
        print('*'+' '*((n//2)-1)+'*'*(n//2))
    elif i>n//2 and i<=n:
        print('*'+' '*(n-1)+'*')
    else :
        print('*')
        
