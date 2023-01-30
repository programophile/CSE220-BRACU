def max_bunch(a):
    temp = 0

    for i in range(len(a)):
        temp2 = 0
        for j in range(i, len(a)):
            if a[i] == a[j]:
                temp2 += 1
            else:
                break
        if temp < temp2:
            temp = temp2
    return temp
print(max_bunch( [1, 2, 2, 3, 4, 4, 4]))