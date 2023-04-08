def array11(array,i):
    if len(array)==i:
        return 0
    if array[i]==11:
        return 1+array11(array,i+1)
    return array11(array,i+1)
print(array11([1,2,11,11,2,3,11],0))