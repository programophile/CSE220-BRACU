def removeAll(source,size,element) :
    for i in range(size):
        if source[i]==element :
            source[i]=0
    print(source)
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)