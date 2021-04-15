import  random
import  string
import os

def genstr():
    strList = []
    for i in range(10):
        strList.append(''.join(random.sample(string.ascii_lowercase, 6)))

    if os.path.exists("str.txt"):
        os.remove("str.txt")
        with open("str.txt","a") as f:
            for str in strList:
                f.writelines(str+'\n')
    else:
        with open("str.txt","a") as f:
            for str in strList:
                f.writelines(str+'\n')
genstr()