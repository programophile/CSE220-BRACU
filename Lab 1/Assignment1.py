def shift_left(source,k) :
    b = 1
    for i in range(k,len(source)) :

        source[i-k]=source[i]
    for i in range(k) :
        source[len(source)-b]=0
        b+=1
    return source
print(shift_left([10,20,30,40,50,60],3))