// Global variables for system
int speed_pin = 8;
double sensor_diameter = 30;   // mm
long cycle_ms = 100; // milliseconds
double speed = 0;              // bike speed of KPH

// Variables in code
int cnt;
unsigned long bg_time;
int pre_data;
int cur_data;
double cycles;
double rotate_speed;

void setup()
{
  // Set the pin mode
  pinMode(speed_pin, INPUT);

  // Configure the variables
  cnt = 0;
  bg_time = millis();
  pre_data = digitalRead(speed_pin);
  cur_data = digitalRead(speed_pin);
  cycles = 0;
  rotate_speed = 0;
  
  // Set the serial
  Serial.begin(9600); // Baud rate
  //Serial.print("Starting to detect speed\n");
}

void loop()
{
  // When the time is still in one checking cycle
  if (millis() < bg_time + cycle_ms)
  {
    // Check wether the input signal changes
    cur_data = digitalRead(speed_pin);
    if(cur_data != pre_data)
    {
      cnt++;
      pre_data = cur_data;
    }
  }
  else // When one checking cycle ends
  {
    // Counts how many cycles the sensor roatate
    cycles = (float)cnt / 40;
    // Convert to rotate speed of RPS
    rotate_speed = cycles / ((double)cycle_ms / 1000);
    // Convert to speed of KPH
    speed = PI * (sensor_diameter / 1000) * rotate_speed * 3.6;
    // Reset the variables
    cnt = 0;
    bg_time = millis();
    // Print the speed
    Serial.println(speed);
  }
}
