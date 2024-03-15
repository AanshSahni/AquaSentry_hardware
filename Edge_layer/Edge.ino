#define SensorPin A0
#define 
String incomingData;
unsigned long int avgValue;
float b;
int buff[10],temp;
// float calibration_value = 21.34;
float calibrationValue = 3.00;


void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.readStringUntil('\n');
    if(incomingData=="A"){
      Serial.println("Turn on water out and water in");
      delay(1000);
    }
    else if(incomingData=="B"){
      Serial.println("Turning on water out and chlorine in");
      delay(1000);
    }
    else{
      Serial.println("Checking for Errors");
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
