def shiftLeft(source,k) :
    b = 1
    for i in range(k,len(source)) :

        source[i-k]=source[i]
    for i in range(k) :
        source[len(source)-b]=0
        b+=1
    print(source)
shiftLeft([10,20,30,40,50,60],3)