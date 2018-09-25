import serial
import threading
import time
import serial.tools.list_ports
from functools import partial

def readSerial(fd):
    print('read serial thread start')
    while True:
        if fd.in_waiting:
            global mainUI
            sdata = fd.readline().decode('UTF-8')
            print(sdata,end='')
            # mainUI.updateLabel(sdata)
        else:
            time.sleep(0.1)

PATH = "E:/PycharmProject/FileOpt/lite_mac.bin"
ser = serial.Serial("COM3", 115200, timeout=0.5)
t1 = threading.Thread(target=readSerial,args=(ser,))
t1.start()

fd = open(PATH, 'rb')
datas = iter(partial(fd.read, 1),b'')
cnt = 0
for data in datas:
    # if (cnt % 256) == 0:
    #     time.sleep(.001)
    ser.write(data)
    cnt += 1
    # time.sleep(.2)
    # print(data)
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
ser.write(b'\xff')
fd.close()

input("发送完成  Total:%d"%(cnt))