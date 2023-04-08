def groupSum(i,array,target):
    if i==len(array):
        return target==0
    return groupSum(i+1,array,target-array[i]) or groupSum(i+1,array,target)
print(groupSum(0,[2,4,8],14))