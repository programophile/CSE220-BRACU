def remove(source,size,inx) :
    for i in range(inx,size):
        source[i]=source[i+1]
    print(source)
remove([10,20,30,40,50,0,0],5,2)