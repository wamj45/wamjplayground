#define RELAY_PIN 5
#define PROX_SENS_PIN 4

void setup() {
  Serial.begin(9600);
  Serial.println("Starting...");

  pinMode(RELAY_PIN, OUTPUT);
  pinMode(PROX_SENS_PIN, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(PROX_SENS_PIN) == LOW) {
    Serial.println("Door is open.\nTurning Lights on!");
    digitalWrite(RELAY_PIN, HIGH);
  }
  else {digitalWrite(RELAY_PIN, LOW);}
  delay(250);
}
