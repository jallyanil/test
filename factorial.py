#factorial numbers = if 5! ,5*4*3*2*1,0!=1 

n = int(input('enter number n'))
if (n<0):
    print('u have entered invalid number')

elif(n==0):
    print('u have entered number 0 is 1')
else:
    mul = 1
    for i in range(1,n+1):
        mul = mul * i
    print('u have entered is{} and factorial is{}'.format(n,mul) )