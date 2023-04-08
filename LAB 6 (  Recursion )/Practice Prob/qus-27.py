def splitArray(array):
    return helper(array,0,0,0)
def helper(array,i,sum1,sum2):
    if i==len(array):
        return sum1==sum2
    return helper(array,i+1,sum1+array[i],sum2) or helper(array,i+1,sum1,sum2+array[i])
print(splitArray([5,2,3]))