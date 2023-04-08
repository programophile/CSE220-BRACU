def split53(array):
    if len(array)==0:
        return 0
    return helper(array,0,0,0)
def helper(array,i,sum1,sum2):
    if i==len(array):
        return sum1==sum2
    if array[i]%5==0:
        return helper(array,i+1,sum1+array[i],sum2)
    elif array[i]%3==0:
        return helper(array,i+1,sum1,sum2+array[i])
    else:
        return helper(array,i+1,sum1+array[i],sum2) or helper(array,i+1,sum1,sum2+array[i])
print(split53([2,4,2]))