int varistor_pin = A0;

void setup() {
  // put your setup code here, to run once:
  // Set the pin mode
  pinMode(varistor_pin, INPUT);
  Serial.begin(9600); // Baud rate
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(analogRead(varistor_pin));
}
