n=eval(input("introduceti nr de zile="))
if (n==29 or n==28):
    print("februarie")
elif n==30:
    print("aprilie,iunie,septembrie,noiembrie")
elif n==31:
    print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
else:
    print("eroare")