def pairStar(str1):
    if len(str1)<2:
        return str1
    if str1[0]==str1[1]:
        return str1[0]+'*'+str1[1]+ pairStar(str1[2:])
    return str1[0]+pairStar(str1[1:])
print(pairStar("xxyy6"))