def StarLab(num):
    if num==1:
        print(1,end="")
    else:
        StarLab(num-1)
        print(num,end="")
def pattern(num,i=0):
    if num==0:
        return
    else:
        pattern(num-1,i+1)
    print(" "*(i), end="")
    StarLab(num)
    print()

pattern(6)