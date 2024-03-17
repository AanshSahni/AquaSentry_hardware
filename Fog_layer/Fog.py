import firebase_admin
from firebase_admin import credentials, db
import serial.tools.list_ports
import serial
import time

# Initialize Firebase Admin SDK
cred = credentials.Certificate("D:/python proj/first-proj-24d5d-firebase-adminsdk-ia69v-0e11754675.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://first-proj-24d5d-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Initialize serial connection
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM ")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

# Reference to the Firebase Realtime Database
ref = db.reference("/ph_data")

# Function to send pH data to Realtime Database
def send_ph_to_realtime_db(ph_data):
    # Set the pH data under a specific key (e.g., "latest")
    ref.child("latest").set({
        "pH": ph_data,
        "timestamp": int(time.time())
    })
    print("pH data sent to Realtime Database")

while True:
    if serialInst.in_waiting:
        # Read pH data from Arduino
        ph_data = serialInst.readline().decode('utf-8').strip()

        # Convert pH data to float
        try:
            ph = float(ph_data)
            print("pH:", ph_data)
            send_ph_to_realtime_db(ph_data)
            if 7.20 <= ph <= 7.60:
                print("The pH of the pool is optimal")
                serialInst.write("O".encode())
            elif ph < 7.20:
                print("The pool is too acidic")
                serialInst.write("A".encode())
                
            elif ph > 7.60:
                print("The pool is too basic")
                serialInst.write("B".encode())
                
            else:
                print("Error: Invalid pH value")
        except ValueError:
            print( ph_data)

    # Wait for some time before reading next pH datacom
    time.sleep(1)  # Adjust as needed
