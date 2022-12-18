A=int(input("Enter number A selected by Alice : "))
B=int(input("Enter number B selected by Bob : "))
g=int(input("Enter base g : "))
p=int(input("Enter modulus p : "))

Xa = (g**A)%p
Xb = (g**B)%p
print("Xa =",Xa)
print("Xb =",Xb)

Ak = (Xb**A)%p
Bk = (Xa**B)%p
print("Secret key Ak =",Ak)
print("Secret key Bk =",Bk)
print("Since Ak=Bk, Alice and Bob can communicate")