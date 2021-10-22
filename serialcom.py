import time

import serial

def pic_input(some_input):
    i = str(input("Please, supply a input for ["+some_input+"]: "))
    return i

serialcom = serial.Serial("COM14", 9600)
serialcom.timeout = 1
var_list = ["Set Point","P","I","D"]


print("\n\nYou are using a P.I.D controller!!\
    \n\nNote:\
    \nSet Point: [Numeric Input]\
    \nP: [Numeric Input]\
    \nI: [Numeric Input]\
    \nD: [Numeric Input]\n")
print('-'*20)
while True:
    out_list = []
    for item in var_list:
        i = pic_input(item)
        if i == "done":
            print("bye!")
            break
        out_list.append(i)
    print('-'*20+"\n")
    print(
    f"Set Point: {out_list[0]}\
    \nP: {out_list[1]} | I: {out_list[2]} | D: {out_list[3]}\n")
    print("-"*20)
    for item in out_list:
        serialcom.write(i.encode())
        time.sleep(0.5)
        print(serialcom.readline().decode("ascii"))
serialcom.close()
