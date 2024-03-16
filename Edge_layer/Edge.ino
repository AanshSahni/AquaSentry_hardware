#define SensorPin A0
#define WaterPump1Pin 9 //out water
#define WaterPump2Pin 10 //in water
#define WaterPump3Pin 11 //chlorine solution
String incomingData;
String incomingsize;

unsigned long int avgValue;
float b;
int buff[10],temp;
float calibrationValue = 3.00;


void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.readStringUntil('\n');
    incomingsize = Serial.readStringUntil("\n");

    if(incomingData=="A"){
      Serial.println("Adjusting water as too acidic...");
      digitalWrite(WaterPump1Pin, HIGH); // Turn on water pump 1
      digitalWrite(WaterPump2Pin, HIGH); // Turn on water pump 2
      delay(500);
      digitalWrite(WaterPump1Pin,LOW);
      digitalWrite(WaterPump2Pin,LOW);
    }
    else if(incomingData=="B"){
      Serial.println("Adjusting water as too basic...");
      digitalWrite(WaterPump1Pin, HIGH); // Turn on water pump 1
      delay(10);
      digitalWrite(WaterPump1Pin,LOW);
      digitalWrite(WaterPump3Pin, HIGH); // Turn on water pump 3
      delay(100);
      digitalWrite(WaterPump3Pin,LOW);
    }
    else if(incomingData=="O"){
      Serial.println("All Good");
      digitalWrite(WaterPump1Pin,LOW);
      digitalWrite(WaterPump2Pin,LOW);
      digitalWrite(WaterPump3Pin,LOW);
    }
    else{
      Serial.println("Checking for Errors");
      // Turn off all pumps if there's an error
      digitalWrite(WaterPump1Pin, LOW);
      digitalWrite(WaterPump2Pin, LOW);
      digitalWrite(WaterPump3Pin, LOW);
      delay(1000);
    }
    delay(5000);
  }
  
  
  for(int i=0;i<10;i++){
    buff[i] = analogRead(SensorPin);
    delay(10);
  }
  for(int i=0;i<9;i++){
    for(int j=i+1;j<10;j++){
      if(buff[i]>buff[j]){
        temp = buff[i];
        buff[i] = buff[j];
        buff[j] = temp;
      }
    }
  }
  avgValue = 0;
  for(int i=2;i<8;i++)
    avgValue+=buff[i];
  
  float phValue = ((float)avgValue * 5.0 / 1024 / 6) + calibrationValue;
  
  Serial.println(phValue,2);
  delay(2000);
}
