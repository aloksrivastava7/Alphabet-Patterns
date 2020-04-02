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
      *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    if i == 1:
        print('*'*n)
    else :
        print(' '*((n//2)-1)+'*')
