def StarLab(num):
    if num==1:
        print(1,end="")
    else:
        StarLab(num-1)
        print(num,end="")
def pattern(num):
    if num==0:
        return
    else:
        pattern(num-1)
    StarLab(num)
    print()

pattern(int(input("Enter N:")))