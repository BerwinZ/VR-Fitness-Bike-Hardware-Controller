int speed_pin = 8;
int pre_data = 0;
int cur_data = 0;
int cnt = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(speed_pin, INPUT);
  Serial.begin(9600);
  Serial.print("Hello World\n"); 
}

void loop() {
  // put your main code here, to run repeatedly:
  cur_data = digitalRead(speed_pin);
  if(cur_data != pre_data)
  {
      cnt++;
      Serial.print(cur_data);
      Serial.print("\nCnt"); 
      Serial.print(cnt);
      Serial.print("\n");
      pre_data = cur_data;
  }
}
