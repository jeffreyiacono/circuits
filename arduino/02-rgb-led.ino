/*

*/

int redPin = 3; // red color to pin 3 on arduino
int greenPin = 5; // green color to pin 5 on arduino
int bluePin = 6; // blue color to pin 6 on arduino

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  setColor(255, 0, 0); // red
  delay(1000);
  setColor(0, 255, 0); // green
  delay(1000);
  setColor(0, 0, 255); // blue
  delay(1000);
  setColor(255, 255, 255); // white
  delay(1000);
  setColor(180, 0, 255); // purple
  delay(1000);
}

void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
