#num=153
#num=str()
#num='-'.join(num)
#print(num)
print('num is armstrong number')
for Num in range(100,2000):
    num=str(Num)
    order=len(num)
    a_num='-'.join(num)
    b_num=a_num.split('-')

#a,b,c=b_num

    b_num=[int(i) for i in b_num ]
    #print(b_num)
    sum=0
    for n in b_num:
    
        sum=sum+n**order
        if sum==int(num):
            print(Num)
            break

    