import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM ")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
dilution_factor = 5.6 
desired_pH = 7.4
Volume = 1.4
chlorine_concentration = 5000

while True:
    if serialInst.in_waiting:
        # Read pH data from Arduino
        ph_data = serialInst.readline().decode('utf-8').strip()

        # Convert pH data to float
        try:
            ph = float(ph_data)
            print("pH:", ph_data)
            ph = float(ph_data)_
            if 7.20 <= ph <= 7.60:
                print("The pH of the pool is optimal")
                serialInst.write("O".encode())
                serialInst.write(b'')  # Placeholder for empty delay
            elif ph < 5.20:
                print("The pool is too acidic")
                serialInst.write("A".encode())
            elif ph > 9.0:
                print("The pool is too basic")
                serialInst.write("B".encode())
            else:
                print("Error: Invalid pH value")
        except ValueError:
            print(ph_data)


