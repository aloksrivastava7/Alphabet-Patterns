'''
Enter Height : 5

	@

	*
	*
	*
	*

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+2):
    if i == 1:
        print('\t@')
    elif i == 2:
         print()
         continue
    else :
        print('\t*')
