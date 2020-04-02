'''

Enter Height : 10

*         *
 *       *
  *     *
   *   *
    * *
     *
     *
     *
     *
     *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for j in range(0,n):
    if j >= (n//2):
        print(' '*((n//2))+'*')
    else :    
        print(' '*j+'*',end = '')
        for k in range(j,(n)-j-1):
            print(' ',end='')
        print('*')
    
            
