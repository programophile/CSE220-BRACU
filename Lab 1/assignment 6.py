def remove_all(source, element):
  b=0
  new_arr = [0]* len(source)
  for i in range(len(source)):
        if source[i]!=element :
            new_arr[b]=source[i]
            b+=1



  print(new_arr)
source=[10,2,30,2,50,2,2,0,0]
remove_all(source,2)