def countX(str1):
    if len(str1)==1:
        if str1[0]=="x":
            return 1
        return 0
    if str1[0]=="x":
        return 1+countX(str1[1:])
    else:
        return countX(str1[1:])
print(countX("hi"))