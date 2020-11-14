  
n = int(input("introduceti numarul n: "))
m= 1
while m<=n:
    s=0
    d=1
    while d<m:
        if not m%d:
            s+=d
        d+=1
    if s==m:
        print(m, "este numar perfect")
    m+=1
