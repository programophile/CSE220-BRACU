def allStar(str1):
    if len(str1)==1:
        return str1
    return str1[0]+"*"+allStar(str1[1:])
print(allStar("hello"))