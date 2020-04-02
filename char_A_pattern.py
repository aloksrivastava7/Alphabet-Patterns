'''

Enter Height : 10

         **
        *  *
       *    *
      *      *
     **********
    *          *
   *            *
  *              *
 *                *
*                  *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    h = 1
    print(' '*(n-i)+'*',end = '')
    while h!=2*i-1:
        if i == (n//2):
            print('*',end = '')
            h = h + 1
        else :    
            print(' ',end='')
            h = h + 1    
    print('*')
    

