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
Volume = 1.5
chlorine_concentration = 0.018
flow = 120

while True:
    if serialInst.in_waiting:
        # Read pH data from Arduino
        ph_data = serialInst.readline().decode('utf-8').strip()

        # Convert pH data to float
        try:
            ph = float(ph_data)
            print("pH:", ph_data)
            ph = float(ph_data)
            Chlorine_to_be_added = (Volume * (desired_pH - ph) * dilution_factor) / (chlorine_concentration * 10)
            print("Chlorine : ", Chlorine_to_be_added)
            Delay_in_seconds = (Chlorine_to_be_added * Volume) / (flow * 3600)

            # Convert delay to milliseconds
            delay_ms = int(Delay_in_seconds * 1000)

            # Check pH level and send commands accordingly
            if 7.20 <= ph <= 7.60:
                print("The pH of the pool is optimal")
                serialInst.write("O".encode())
                serialInst.write(b'')  # Placeholder for empty delay
            elif ph < 7.20:
                print("The pool is too acidic")
                serialInst.write("A".encode())
                serialInst.write(str(delay_ms).encode())  # Send delay value in milliseconds as string
                print(delay_ms)
            elif ph > 7.60:
                print("The pool is too basic")
                serialInst.write("B".encode())
                serialInst.write(str(delay_ms).encode())  # Send delay value in milliseconds as string
                print(delay_ms)
            else:
                print("Error: Invalid pH value")
        except ValueError:
            print(ph_data)
