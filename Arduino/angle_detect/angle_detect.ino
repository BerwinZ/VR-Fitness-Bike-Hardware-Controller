int varistor_pin = A0;
double raw_data = 0;
double negative45point = 81;
double negative0point = 349;
double positive0point = 500;
double positive45point = 832;
double fullpointAngle = 30;
double angle = 0;
double k1, b1, k2, b2;

void setup() {
  // put your setup code here, to run once:
  // Set the pin mode
  pinMode(varistor_pin, INPUT);
  k1 = 30.0 / (negative0point - negative45point);
  b1 = -1 * negative0point * k1;
  k2 = 30.0 / (positive45point - positive0point);
  b2 = -1 * positive0point * k2;
  Serial.begin(9600); // Baud rate
}

void loop() {
  // put your main code here, to run repeatedly:
  double raw_data = analogRead(varistor_pin);
  if(raw_data <= 3)
  {
    angle = -fullpointAngle;
  }
  else if(raw_data > 3 && raw_data < negative0point)
  {
    angle = k1 * raw_data + b1;
  }
  else if(raw_data > positive0point && raw_data < 1020)
  {
    angle = k2 * raw_data + b2;
  }
  else if(raw_data >= 1020)
  {
    angle = fullpointAngle;
  }
  else
  {
    angle = 0;
  }

//  Serial.println(raw_data);
  Serial.println(angle);
}
