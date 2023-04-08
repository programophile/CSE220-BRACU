def countPairs(str1):
    if len(str1)<3:
        return 0
    if str1[0]==str1[2]:
        return 1+countPairs(str1[1:])
    return countPairs(str1[1:])
print( countPairs("axbx"))