int tempPin=A1;

int tempValue=0;
void setup() {
Serial.begin(9600);
}

void loop() {
tempValue =  analogRead(tempPin);
tempValue=(5*tempValue*100)/1024;

Serial.println(tempValue);

delay(1000);

}
