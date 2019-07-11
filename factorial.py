#fact using function
fact=1
def fac(n):
    if n<0:
        return -1
    elif n==0:
        return 1
    else:
        return(n*fac(n-1))
n=int(input("Enter n"))
print(fac(n))


#fact using for loop
n=int(input("enter n"))
fact=1
for i in range(1,n+1):
    fact=fact*i
        
    print(fact)
