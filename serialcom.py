import time

import matplotlib.pyplot as plt
import serial


def pic_input(some_input):
    """
    Read Input from console.

    Args [some_input]: Input name.
    type: str

    return: Input value
    rtype: str
    """
    i = str(input("Please, supply a input for [" + some_input + "]: "))
    return i


def validate(some_input):
    """
    Validate Input from console.

    Args [some_input]: Input value.
    type: str

    return: Input value and bool representing validity of the input provided
    rtype: tuple
    """
    try:
        some_int = str(int(some_input))
        return some_input, True
    except:
        print("Input invalid...")
        return "", False


def terminator(some_string):
    """
    Add terminator for values under 4 chars so that the pic can process it accordingly.

    Args [some_input]: Input value.
    type: str

    return: Input value with terminator
    rtype: str
    """
    if len(some_string) < 4:
        some_string = some_string + ";"
    return some_string


serialcom = serial.Serial("COM7", 9600)
serialcom.timeout = 0.5

print(
    "\n\nYou are using a P.I.D controller!!\
    \n\nNote:\
    \nPWM: [Numeric Input]\n"
)
print("-" * 20)
adc_list = []

while True:
    counter = 0
    done = False
    i = pic_input("PWM")
    if i == "done":
        print("bye!")
        break
    i, some_bool = validate(i)

    while some_bool == False:
        i, some_bool = pic_input("PWM")
        if i == "done":
            print("bye!")
            done = True
            break
    if done == True:
        break

    i = terminator(i)
    serialcom.write(i.encode())
    time.sleep(0.1)

    while counter < 20:
        adc = serialcom.readline().decode("ascii")
        print(adc)
        adc_list.append(adc)
        counter = counter + 1
# remove invalid readings
adc_list = [int(x[:-1]) for x in adc_list if x != ""]
print(adc_list)
# plot
plt.plot(adc_list)
plt.ylabel("ADC readings")
plt.show()

serialcom.close()
