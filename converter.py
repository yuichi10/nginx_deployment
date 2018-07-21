import smbus
from time import sleep

bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x04

def writeCommand(cmd):
    bus.write_byte(SLAVE_ADDRESS, cmd)
    print("send: ",cmd)

def readValue():
    val = bus.read_byte(SLAVE_ADDRESS)
    return val

while True:
    command = raw_input("Enter command : ")
    if command == 'r0':
        writeCommand(0)
        receivedValue = readValue()
        print("received value from A0: ",receivedValue)
    elif command == 'r1':
        writeCommand(1)
        receivedValue = readValue()
        print("received value from A1: ",receivedValue)
    elif command == 'r2':
        writeCommand(2)
        receivedValue = readValue()
        print("received value from A2: ",receivedValue)
    elif command == 'r3':
        writeCommand(3)
        receivedValue = readValue()
        print("received value from A3: ",receivedValue)
    elif command == 'r4':
        writeCommand(4)
        receivedValue = readValue()
        print("received value from A4: ",receivedValue)
    elif command == 'r5':
        writeCommand(5)
        receivedValue = readValue()
        print("received value from A5: ",receivedValue)
