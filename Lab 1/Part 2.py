def findmean(source):
  mean=0
  for i in range(len(source)) :
    mean+= source[i]
  return float(mean/len(source))
# findmean([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])


def standered_deviation(source):
  count = 0
  for i in range(len(source)):
    count += (source[i] - findmean(source)) ** 2
  return (count / (len(source) - 1)) ** 0.5


# standered_deviation([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])


def new_arry(source):
  val = findmean(source) + (1.5 * standered_deviation(source))
  new_arr = [0] * len(source)
  count = 0
  for i in range(len(source)):
    if source[i] >= val or (0 > source[i] >= -val):
      new_arr[count] = source[i]
      count += 1
  new_arr2 = [0] * count

  for i in range(count):
    new_arr2[i] = new_arr[i]
  return new_arr2


print(new_arry([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]))
