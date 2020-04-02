'''

Enter Height : 15

***************
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
*******

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1:
        print('*'*n)
        i = i + 1
    elif i == n:
        print('*'*(n//2))
        i = i + 1
    else:
        print(' '*(n//2)+'*'+' '*(n//2))
        
