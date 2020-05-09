print('num is armstrong number')
lower=100
upper=2000
for Num in range(lower,upper+1):
    num=str(Num)
    order=len(num)
    a_num='-'.join(num)
    b_num=a_num.split('-')

    b_num=[int(i) for i in b_num ]
    #print(b_num)
    sum=0
    for n in b_num:
    
        sum=sum+n**order
        if sum==int(num):
            print(Num)
            break

    
