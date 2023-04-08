def countAbc(str1):
    if len(str1)<3:
        return 0
    if str1[0:3]=="abc"or str1[0:3]=="aba":
        return 1+countAbc(str1[3:])
    return countAbc(str1[1:])
print(countAbc("abaxxabc"))