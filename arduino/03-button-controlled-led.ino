/*

*/
int ledPin = 5;
int buttonApin = 9; // one button, pin 9 on arduino
int buttonBpin = 8; // second button, pin 8 on arduino
byte leds = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonApin, INPUT_PULLUP);
  pinMode(buttonBpin, INPUT_PULLUP);
}

void loop() {
  if(digitalRead(buttonApin) == LOW) {
    digitalWrite(ledPin, HIGH);
  }

  if(digitalRead(buttonBpin) == LOW) {
    digitalWrite(ledPin, LOW);
  }
}
