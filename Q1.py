# Encyrption

s=input("Enter plain text : ")
k=int(input("Enter key : "))
ans=""
for i in s:
    if i==" ":
        ans+="0"
    else:
        ans+=chr((ord(i)+k-97)%26+97)
print("Encrypted text is :",ans)


# Decryption

s=input("Enter encrypted text : ")
k=int(input("Enter key : "))
ans=""
for i in s:
    if i=="0":
        ans+=" "
    else:
        ans+=chr((ord(i)-k-97+26)%26+97)
print("Plain text is :",ans)