num=10
for i in range(0,7):
    for n in range (0,7):
        if i+n==3 or n-i==3 or i-n==3 or i+n==9:
            print('*',end=' ')
        else:
            print(end='  ')
    
    print()
    