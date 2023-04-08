def splitOdd(array):
    if len(array)==0:
        return False
    return helper(array,0,0,0)
def helper(array,i,sum1,sum2):
    if i==len(array):
        return sum1%10==0 and sum2%2!=0
    if array[i]%10==0 and array[i]%2!=0:
        return helper(array,i+1,sum1+array[i],sum2)
    return helper(array,i+1,sum1+array[i],sum2) or helper(array,i+1,sum1,sum2+array[i])
print(splitOdd([5,5,5]))