'''

Enter Height : 5

*
*    *
*   *
*  *
* *
* *
*  *
*   *
*    *
*
*

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == (n//2):
        for j in range(1,n):
            print('*'+' '*(n-j)+'*')
            i = i + 1
    elif i == (n//2)+1:
         for k in range(1,n):
             print('*'+' '*(k)+'*')
             i = i + 1        
    else :
        print('*')
        
