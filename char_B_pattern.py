'''

Enter Height : 15

*******
*      *
*      *
*      *
*      *
*      *
*******
*      *
*      *
*      *
*      *
*      *
*      *
*      *
*******


'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == (n//2) or i == n:
        print('*'*(n//2))
    else :
        print('*'+' '*((n//2)-1)+'*')
        
