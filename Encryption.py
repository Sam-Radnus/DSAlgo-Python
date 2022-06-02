from cryptography.fernet import Fernet
message = "sam sundar "
key=Fernet.generate_key()
fernet=Fernet(key)
encMessage=fernet.encrypt(message.encode())  #enc message is a byte string
encMessage2=fernet.encrypt(str(encMessage).encode())
print(type(encMessage))
print(message)
print(encMessage)
print(encMessage2)
print(fernet.decrypt(encMessage).decode())
print(fernet.decrypt(encMessage2).decode())
