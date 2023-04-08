def stringClean(str1):
    if len(str1)<2:
        return str1
    if str1[0]==str1[1]:
        return stringClean(str1[1:])
    return str1[0]+stringClean(str1[1:])
print(stringClean("yyzzza"))