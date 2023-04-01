def flatten_list(given_list,output_list):

  if isinstance(given_list,list) :
    for i in given_list:
      flatten_list(i,output_list)


  else:
    output_list.append(given_list)
  return output_list
nested_list=[1,[2,[[3,[4],5]],6],8,8]
print(flatten_list(nested_list,[]))