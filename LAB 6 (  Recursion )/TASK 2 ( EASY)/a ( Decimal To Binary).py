def decimaltobinary(dec, str1):
    if dec // 2 == 0:
        str1 += str(dec % 2)
        return str1[::-1]
    else:
        str1 += str(dec % 2)
        return decimaltobinary(dec // 2, str1)



print(decimaltobinary(10, ""))
