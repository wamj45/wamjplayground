#include <Servo.h>

#define   PAN_SERVO_PIN     9
#define   TILT_SERVO_PIN    10
#define   PAN_BUTTON        3
#define   TILT_BUTTON       4

Servo panServo;
Servo tiltServo;

int pos = 0;
int delayTime = 5;

// Servo can handle 270degs of motion
void respondNo()
{
  Serial.println("RUDDE saying no");
  for (pos = 0; pos <= 270; pos += 1) {
    panServo.write(pos);
    delay(delayTime);
  }

  for (pos = 270; pos >= 0; pos -= 1) {
    panServo.write(pos);
    delay(delayTime);
   }
}

void respondYes()
{
  Serial.println("RUDDE saying yes");
  for (pos = 0; pos <= 270; pos += 1) {
    testServo.write(pos);
    delay(delayTime);
  }

  for (pos = 270; pos >= 0; pos -= 1) {
    testServo.write(pos);
    delay(delayTime);
   }
}

void setup() {
  Serial.begin(9600);
  panServo.attach(PAN_SERVO_PIN);
  tiltServo.attach(TILT_SERVO_PIN);

  pinMode(PAN_BUTTON, INPUT);
  // pinMode(TILT_BUTTON, INPUT);

  Serial.println("Starting Servo Control!");
}

void loop() {
  if (digitalRead(PAN_BUTTON) == HIGH) {respondNo();}
  // if (digitalRead(TILT_BUTTON) == HIGH) {respondYes();}
  delay(500)
}
