n=eval(input("introduceti nr n: "))
s1=0
s2=0
r2=0
for i in range(1,(n+1)):
    s1+=i**3
    r2+=i
    s2=r2**2
if s1>s2:
    print("s1 este mai mare decat s2")
if s1<s2:
    print("s1 este mai mic decat s2")
if s1==s2:
    print("s1 este egal cu s2")
n=eval(input("introduceti nr n: "))
s3=0
r3=0
s4=0
r4=0
t4=0
for i in range (1,(n+1)):
    r3=i**2
    s3=3*r3
    r4+=i
    s4=n**3+n**2+r4
if s3>s4:
    print("s3 este mai mare decat s4")
if s3<s4:
    print("s3 este mai mic decat s4")
if s3==s4:
    print("s3 este egal cu s4")
