# import self as self


class HashTable:
  def __init__(self,length):
    self.length=length
    self.array=[0]*length

  def hash_calc(self,str1):
    self.str1 = str1
    consunent=0
    dighit_sum=0
    for i in range(len(self.str1)):
      if 'A'<=self.str1[i]<='Z':
        if i not in ["A","E","I","O","U"]:
          consunent+=1
      else:
        dighit_sum+=int(i)
    self.index=((consunent*24)+dighit_sum)%9
    if self.array[self.index]!=0:
      self.index=self.LinarProbing()
    self.array[self.index]=self.str1
    return self.index
  def LinarProbing(self):
    for i in range(self.index,self.length):
      if self.array[i]==0:
        return i
  def Print_hasharray(self):
    print(self.array)
b=HashTable(9)
b.hash_calc('ST1E89B8A32')
b.hash_calc("hahj6")
b.Print_hasharray()


# print(hash_calc('ST1E89B8A32'))
