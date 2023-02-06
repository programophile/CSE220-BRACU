input1 = input("")
input2 = input("")
start_index1 = 0
start_index2 = 0
start_letter1 = ""
start_letter2 = ""
last_input = ""
mul_arr = [[""] * 10, [""] * 10]
count = 0
if len(input1) > 10 or len(input2) > 10:
    print("Invalid input")
else:
    for i in range(len(input1)):
        mul_arr[0][i] = input1[i]
        if 64 < ord(input1[i]) < 91:
            start_index1 = i
            start_letter1 = input1[i]
    for j in range(len(input2)):
        mul_arr[1][j] = input2[j]
        if 64 < ord(input2[j]) < 91:
            start_index2 = j
            start_letter2 = input2[j]
    print(
        f"Top borad charecter : {start_letter1} \nTop index : {start_index1}\nBottom charecter : {start_letter2} \nBottom index:{start_index2}")
    while True:
        last_input = input("Enter promt :")
        if last_input == ("q" or "Q"):
            break
        else:
            index1 = 0 + count
            index2 = len(input2)-2-count
            for i in range(10):
                index1 = (index1 + 1) % 10
                print(mul_arr[0][index1], end="")
            print()
            count += 1
            for j in range(10):
                index2 = (index2 +1) % 10
                # print(index2)
                print(mul_arr[1][index2], end="")
            print()