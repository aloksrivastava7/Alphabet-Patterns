'''

Enter Height : 15

 *                            *
  *                          *
   *                        *
    *                      *
     *                    *
      *                  *
       *                *
        *              *
         *            *
          *          *
           *        *
            *      *
             *    *
              *  *
               **

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    print(' '*i+'*',end = '')
    for j in range(i,(2*n)-i):
        print(' ',end='')
    print('*')
