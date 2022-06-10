text = input("Enter a One Word LowerCase Messages")
distance = int(input("Enter the Distance Values"))
code = ""
res = ""
for ch in text:
    ordValue = ord(ch)
    cipherVal = ordValue + distance
    originalVal = cipherVal - distance
    if cipherVal > ord('z'):
        cipherVal = ord('a') + distance - (ord('z') - ordValue + 1)
        originalVal = ord('a') + distance - (ord('z') - ordValue + 1)
    code += chr(cipherVal)
    res += chr(originalVal)
print(code)
print(res)
