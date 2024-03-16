import serial.tools.list_ports

start = True

size_dict = {'demo': 1, 'small': 2, 'medium': 3, 'large': 4}

fire_size = "demo"

pool_size = None

for size, num in size_dict.items(): 
    if size == fire_size:
        pool_size = num


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

while (start):
    if serialInst.in_waiting:
        # Read pH data from Arduino
        ph_data = serialInst.readline().decode('utf-8').strip()

        # Convert pH data to float
        try:
            ph = float(ph_data)
            print("pH:", ph_data)
            ph = float(ph_data)
            if 7.20 <= ph <= 7.60:
                print("The pH of the pool is optimal")
                serialInst.write("O".encode())
                serialInst.write(pool_size.encode())
            elif ph < 7.20:
                print("The pool is too acidic")
                serialInst.write("A".encode())
                serialInst.write(pool_size.encode())
            elif ph > 7.60:
                print("The pool is too basic")
                serialInst.write("B".encode())
                serialInst.write(pool_size.encode())
            else:
                print("Error: Invalid pH value")
        except ValueError:
            print(ph_data)


