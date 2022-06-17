import os

currentDirectoryPath = os.getcwd()
listofFileNames = os.listdir("C:\Sam Sundar")
print(currentDirectoryPath)
for name in listofFileNames:
    if name.endswith(".py"):
        print(name)
    else:
        print(name)