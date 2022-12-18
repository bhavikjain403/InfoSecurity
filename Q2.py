def getKey(s,k):
    if len(s)==len(k):
        return k
    diff=len(s)-len(k)
    for i in range(diff):
        k+=(k[i%len(k)])
    return k

# Encryption

s=input("Enter plain text without spaces : ").upper()
k=input("Enter key : ").upper()

def encrypt(s,k):
    k=getKey(s,k)
    ans=""
    for i in range(len(s)):
        ans += chr(ord("A") + (ord(s[i]) + ord(k[i]))%26)
    return ans

print("The cipher text is :",encrypt(s,k))


# Decryption

s=input("Enter cipher text : ").upper()
k=input("Enter key : ").upper()

def decrypt(s,k):
    k=getKey(s,k)
    ans=""
    for i in range(len(s)):
        ans += chr(ord("A") + (ord(s[i]) - ord(k[i]) +26 )%26)
    return ans

print("The plain text is :",decrypt(s,k))