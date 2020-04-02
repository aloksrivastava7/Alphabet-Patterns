'''

Enter Height : 15

**                             **
* *                           * *
*  *                         *  *
*   *                       *   *
*    *                     *    *
*     *                   *     *
*      *                 *      *
*       *               *       *
*        *             *        *
*         *           *         *
*          *         *          *
*           *       *           *
*            *     *            *
*             *   *             *
*              * *              *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for j in range(0,n):
    print('*'+' '*j+'*',end = '')
    for k in range(j,(2*n)-j-1):
        print(' ',end='')
    print('*'+' '*((2*n-k)-2)+'*')
