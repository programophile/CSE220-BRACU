def split_array(a) :
  temp=0
  for i in range(len(a)) :
    temp+=a[i]
    temp2=0
    for j in range(i+1,len(a)):
      temp2+=a[j]
    if temp==temp2 :
      return True
  return False
print(split_array([2, 1, 1, 2, 1]))