n=int(input("introduceti varsta lui Mihai: "))
c=1
if n<20:    
    for i in range(1,n+1):
        if (i==1):
            c=c+2
        else:
            c=(c*2)+i
print("La varsta de",n,"ani Mihai a primit:",c,"$")
print("Cadoul lui Mihai a fost mai mare de 100$ la 6 ani")