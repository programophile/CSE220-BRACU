n=int(input("Enter N :"))
arr=input("Enter arr :")
cir_arr = [0]*int(n)
count=0
for i in range(len(arr)):
    if arr[i] != " ":
        cir_arr[count]= arr[i]
        count+=1
for j in range(n) :
    a = True
    for k in range(j,n+j):
        if int(cir_arr[k%n])>int(cir_arr[j]):
            print(cir_arr[k%n], end=" ")
            a=True
            break
        else :
            a = False
    if a==False :
        print("-1",end=" ")


