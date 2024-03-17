#define SensorPin A0
#define WaterPump1Pin 5 //out water
#define WaterPump2Pin 9 //in water
#define WaterPump3Pin 11 //chlorine solution
String incomingData;

unsigned long int avgValue;
float b;
int buff[10],temp;
float calibration_value = 21.84;

void setup() {
  Serial.begin(9600);
  pinMode(WaterPump1Pin, OUTPUT);
  pinMode(WaterPump2Pin, OUTPUT);
  pinMode(WaterPump3Pin, OUTPUT);
}

void loop() {
  analogWrite(WaterPump1Pin, 0);
  analogWrite(WaterPump2Pin, 0);
  analogWrite(WaterPump3Pin, 0);
  if (Serial.available() > 0) {
    incomingData = Serial.readStringUntil('\n');
    if (incomingData == "A") {
      Serial.println("Adjusting water as too acidic...");
      analogWrite(WaterPump3Pin,0);
      analogWrite(WaterPump1Pin, 155); // Turn on water pump 1
      analogWrite(WaterPump2Pin, 155); // Turn on water pump 2
      
      delay(5000);
      analogWrite(WaterPump1Pin,0);
      analogWrite(WaterPump2Pin,0);

    } 
    else if (incomingData == "B") {
      Serial.println("Adjusting water as too basic...");
      analogWrite(WaterPump2Pin, 0);
      analogWrite(WaterPump1Pin, 155); // Turn on water pump 1
      analogWrite(WaterPump3Pin, 155);
      delay(5000);
      analogWrite(WaterPump1Pin, 0); // Turn on water pump 3
      analogWrite(WaterPump3Pin, 0);
    } 
    else if (incomingData == "O") {
      Serial.println("All Good");
      analogWrite(WaterPump1Pin, 0);
      analogWrite(WaterPump2Pin, 0);
      analogWrite(WaterPump3Pin, 0);
    } 
    else {
      Serial.println("Checking for Errors");
      // Turn off all pumps if there's an error
      analogWrite(WaterPump1Pin, 0);
      analogWrite(WaterPump2Pin, 0);
      analogWrite(WaterPump3Pin, 0);
      delay(5000);
    }
    delay(5000); // Add delay between serial reads
  }

  for (int i = 0; i < 10; i++) {
    buff[i] = analogRead(SensorPin);
    delay(10);
  }
  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 10; j++) {
      if (buff[i] > buff[j]) {
        temp = buff[i];
        buff[i] = buff[j];
        buff[j] = temp;
      }
    }
  }
  avgValue = 0;
  for (int i = 2; i < 8; i++)
    avgValue += buff[i];

  float volt = (float)avgValue * 5.0 / 1024 / 6;
  float ph_act = -5.70 * volt + calibration_value;

  Serial.println(ph_act, 2);
  delay(5000); // Adjust delay based on sensor reading frequency
}
