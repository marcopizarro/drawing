/*
 * READ ME
 * 
 * Connect two buttons to arduino.
 * 
 * 1: One leg to ground, other to Digital 3
 * 2: One leg to ground, other to Digital 4
 */

const int buttonPin = 3;     // the number of the pushbutton pin
const int buttonPin1 = 4;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;   
int buttonState1 = 0; // variable for reading the pushbutton status

void setup() {
  Serial.begin(115200);
  // initialize the LED pin as an output:
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT_PULLUP);
    pinMode(buttonPin1, INPUT_PULLUP);
}

void loop() {
  // read the state of the pushbutton value:
  int sensorValue = 0;
  buttonState = digitalRead(buttonPin);
  buttonState1 = digitalRead(buttonPin1);

  if (buttonState == LOW) {
    sensorValue = 1;
  } else if(buttonState1 == LOW) {
     sensorValue = 2;
  }
  Serial.write( sensorValue );
  delay(500);
}
