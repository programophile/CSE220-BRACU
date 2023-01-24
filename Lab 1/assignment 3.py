def shiftRight(source,k) :
    for i in range(k,len(source)) :
        source[i]=source[i-k]
        source[i-k]=0
    print(source)
shiftRight([10,20,30,40,50,60],3)