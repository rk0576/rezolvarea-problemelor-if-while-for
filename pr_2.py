n=eval(input("introduceti n: "))
s=0
p=1
for i in range(1,n+1):
    p*=i
    s+=p
print("suma este: ",s,)
