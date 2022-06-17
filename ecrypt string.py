def encrypt(sttr,enkey):
    return enkey.join(sttr)

def decrypt(sttr,enkey):
    return sttr.split(enkey)

##main##
 mainString =input("Enter main string:")
 encryptStr =input("Enter encryption key:")
 enstr      =encrypt(mainString,encryptStr)
 deLst      =decrypt(enStr,encryptStr)

deStr="".join(deLst)
print("the encrypted string is :",enStr)
print("string after decryption is:" ,deStr)