  
a=eval(input("introduceti lungimea laturii 1: "))
b=eval(input("introduceti lungimea laturii 2: "))
c=eval(input("introduceti lungimea laturii 3: "))
if ((a>0)and(b>0)and(c>0)):
    if ((a<b+c)and(b<a+c)and(c<b+c)):
        print("exista")
        if ((a==b)and(b==c)and(a==c)):
            print("este echilateral")
        if ((a!=b)and(b!=c)and(c!=a)):
            print("este scalen")
        if (((a!=b)or(b!=c)or(c!=a))and((a==b)or(b==c)or(a==c))):
            print("este isoscel")
    else:
        print("nu exista")
