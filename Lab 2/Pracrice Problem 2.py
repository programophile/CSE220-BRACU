# def cir_arry(array,size,start) :
#     k=start
#     for i in range(size) :
#         print(array[k])
#
#         # k+=1
#         k = (k+1) % len(array)
#     print(array)
# cir_arry([1,2,0,0,3,4,5],5,4)

# def cir_rotation(cir_array,size,st1) :
#     index=st1+size
#
#
#     for i in range(index,st1,-1):
#         cir_array[(i)%(len(cir_array))]= cir_array[(i-1)%len(cir_array)]
#     cir_array[st1]=0
#     # for i in range(size+st1-1,st1+1,-1):
#     #    print(i)
#     #    cir_array[(i)%len(cir_array)]=cir_array[(i-1)%len(cir_array)]
#     print(cir_array)
# cir_rotation([1,2,3,0,0,4,5],5,5)

def reverseSub(cir1,st1,size,m,n,newstart) :
    sub_arr=[0] * (n-m+1)
    index_sub=newstart
    for i in range(m,n+1):
        sub_arr[index_sub%(n-m+1)]=cir1[i%len(cir1)]
        index_sub+=1
    rev_arr= [0]*(n-m+1)
    rev_arr_start=newstart
    for i in range(newstart+n-m,newstart-1,-1) :
        rev_arr[rev_arr_start%(n-m+1)]=sub_arr[i%(n-m+1)]
        rev_arr_start+=1
    for i in range(n-m+1) :
        for j in range(i+1,n-m+1) :
            print(rev_arr[i]+rev_arr[j])
reverseSub([1,2,3,0,0,5,6],5,5,6,8,2)
