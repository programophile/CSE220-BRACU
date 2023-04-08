def changePi(str1):
    if len(str1[0:])<2:
        if str1[0:]=="pi":
            return "3.1416"
        return str1[0:]
    if str1[0:2]=="pi":
        return "3.1416"+ changePi(str1[2:])
    else:
        return str1[0]+changePi(str1[1:])
print(changePi('ppix'))