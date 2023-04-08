def strDist(str1,str2):
    if len(str1)<len(str2):
        return 0
    if str1[:len(str2)]==str2:
        if str1[-len(str2):]==str2:
            return len(str1)
        else:
            return strDist(str1[:-1],str2)
    return strDist(str1[1:],str2)
print( strDist("catcowcat", "cow"))