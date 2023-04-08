def nestParen(str1):
    if len(str1)==0:
        return True
    if str1[0]=="(" and str1[len(str1)-1]==")":
        return  nestParen(str1[1:len(str1)-1])
    return False
print(nestParen("((()))"))