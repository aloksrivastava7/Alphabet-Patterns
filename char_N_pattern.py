'''

Enter Height : 15

**             *
* *            *
*  *           *
*   *          *
*    *         *
*     *        *
*      *       *
*       *      *
*        *     *
*         *    *
*          *   *
*           *  *
*            * *
*             **

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i==1:
        for j in range(0,n-1):
            print('*'+' '*j+'*'+' '*(n-j-2)+'*')        
   
