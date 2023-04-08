def array6(array,i):
    if i==len(array):
        return False
    if array[i]==6:
        return True
    return array6(array,i+1)
print(array6([6],0))