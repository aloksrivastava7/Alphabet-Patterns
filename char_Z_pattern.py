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
***************

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'*n)
    elif i == 2:
        for j in range(1,n-1):
            print(' '*(n-j-1)+'*')
