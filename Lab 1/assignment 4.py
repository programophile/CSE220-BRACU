def rotateRight(source,k) :
    for i in range(k,len(source)) :
        temp=source[i]
        source[i]=source[i-k]
        source[i-k]=temp
    print(source)
rotateRight([10,20,30,40,50,60],3)