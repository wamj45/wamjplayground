#include <Servo.h>

#define ServoPin 9

Servo testServo;
int pos = 0;
int delayTime = 2;

void setup() {
  Serial.begin(9600);
  testServo.attach(ServoPin);

  Serial.println("Starting Servo Control!");

}

void loop() {
  Serial.println("Moving the servo in the positive dir...");
  for (pos = 0; pos <= 180; pos += 1) {
    testServo.write(pos);
    delay(delayTime);
  }

  Serial.println("Moving the servo in the negative dir...");
  for (pos = 180; pos >= 0; pos -= 1) {
    testServo.write(pos);
    delay(delayTime);
   }
}
