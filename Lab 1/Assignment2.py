def rotate_left(source,k) :
    b = 0
    for i in range(k,len(source)) :
        temp=source[i-k]
        source[i-k]=source[i]
        source[len(source)-k+b]=temp
        b+=1
    return source
print(rotate_left([10,20,30,40,50,60],3))