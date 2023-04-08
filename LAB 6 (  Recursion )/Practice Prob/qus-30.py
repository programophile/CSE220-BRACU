def groupSum5(i,array,target):
    if len(array)==0:
        return array[0]==sum
    return helper(i,array,target,0)
def helper(i,array,target,sum):
    if i==len(array):
        return sum==target
    # if sum==target:
    #     return True
    if array[i]%5==0:
        if array[i+1]==1 and i!=len(array)-2:
            return helper(i+2,array,target,sum+array[i])
        return helper(i+1,array,target,sum+array[i])
    return helper(i+1,array,target,sum) or helper(i+1,array,target,sum+array[i])
print(groupSum5(0,[2,5,10,4],12))

