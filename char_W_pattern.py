'''

Enter Height : 15

*              **              *
*             *  *             *
*            *    *            *
*           *      *           *
*          *        *          *
*         *          *         *
*        *            *        *
*       *              *       *
*      *                *      *
*     *                  *     *
*    *                    *    *
*   *                      *   *
*  *                        *  *
* *                          * *
**                            **

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    h = 1
    print('*'+' '*(n-i)+'*',end = '')
    while h!=2*i-1:
        print(' ',end='')
        h = h + 1    
    print('*'+' '*(n-i)+'*')
