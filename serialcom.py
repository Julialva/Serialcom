import time

import serial


def pic_input(some_input):
    i = str(input("Please, supply a input for [" + some_input + "]: "))
    return i


def validate(some_input):
    try:
        some_int = str(int(some_input))
        return some_input, True
    except:
        print("Input invalid...")
        return invalid_list(), False


def terminator(some_string):
    if len(some_string) < 4:
        some_string = some_string + ";"
    return some_string


def invalid_list():
    return ["Invalid", "Invalid", "Invalid", "Invalid"]


serialcom = serial.Serial("COM14", 9600)
serialcom.timeout = 1
var_list = ["Set Point", "P", "I", "D"]


def pretty_text(out_list):
    print("-" * 20 + "\n")
    print(
        f"Set Point: {out_list[0]}\
    \nP: {out_list[1]} | I: {out_list[2]} | D: {out_list[3]}\n"
    )
    print("-" * 20)


print(
    "\n\nYou are using a P.I.D controller!!\
    \n\nNote:\
    \nSet Point: [Numeric Input]\
    \nP: [Numeric Input]\
    \nI: [Numeric Input]\
    \nD: [Numeric Input]\n"
)
print("-" * 20)

while True:
    out_list = []
    done = False
    for item in var_list:
        i = pic_input(item)
        if i == "done":
            print("bye!")
            done = True
            break

        i, some_bool = validate(i)

        if some_bool == False:
            break
        out_list.append(i)

    if done:
        break
    pretty_text(out_list)

    for item in out_list:
        item = terminator(item)
        serialcom.write(item.encode())
        time.sleep(0.5)
        print(serialcom.readline().decode("ascii"))
serialcom.close()
