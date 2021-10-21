import time

import serial

serialcom = serial.Serial("COM3", 9600)
serialcom.timeout = 1

while True:
    i = str(input("input (on/off): ")).strip().lower()
    if i == "done":
        print("bye!")
        break
    serialcom.write(i.encode())
    time.sleep(0.5)
    print(serialcom.readline().decode("ascii"))
serialcom.close()
