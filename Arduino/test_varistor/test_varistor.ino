int varistor_pin = A0;
double angle = 0;
double curr2ang_rate = 20;

void setup() {
  // put your setup code here, to run once:
  // Set the pin mode
  pinMode(varistor_pin, INPUT);
  Serial.begin(9600); // Baud rate
}

void loop() {
  // put your main code here, to run repeatedly:
  double raw_data = analogRead(varistor_pin);
  angle = (raw_data + 42 - 512) / curr2ang_rate;
//  if (550 < raw_data && raw_data < 651) {
//    angle = 0;
//  } else if (450 < raw_data && raw_data < 551) {
//    angle = -1; 
//  } else if (350 < raw_data && raw_data < 451) {
//    angle = -2; 
//  } else if (raw_data < 351) {
//    angle = -3; 
//  } else if (650 < raw_data && raw_data < 751) {
//    angle = 1; 
//  } else if (750 < raw_data && raw_data < 851) {
//    angle = 2; 
//  } else if (850 < raw_data) {
//    angle = 3;
//  }
//  Serial.println(raw_data);
  Serial.println(angle);
}
