def remove(source,size,inx) :
    for i in range(inx+1,size):
        source[i-1]=source[i]
    source[size-1]=0
    print(source)
remove([10,20,30,40,50,0,0],5,2)