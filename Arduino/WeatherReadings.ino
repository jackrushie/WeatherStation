#include <dht11.h>
#define DHT11PIN 7

dht11 DHT11;
int LightsensorValue;
int AirsensorValue;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.println();
  
  //Light Sensor
  LightsensorValue = analogRead(0); 
  //Serial.print("Light Level:");
  Serial.print(LightsensorValue, DEC);
  Serial.print(","); 
  
  // Air Sensor
  
  AirsensorValue = analogRead(5);       // read analog input pin 5
  //Serial.print("Air Quality:");
  Serial.print(AirsensorValue, DEC);
  Serial.print(","); 
  // prints the value read
  //Serial.println(" PPM");

  // Temp and Humidity Sensor
  int chk = DHT11.read(DHT11PIN);

  //Serial.print("Humidity (%): ");
  Serial.print((float)DHT11.humidity, 2);
  Serial.print(",");
  //Serial.print("Temperature (C): ");
  Serial.print((float)DHT11.temperature, 2);
  Serial.print(",");

  //end
  delay(300000);

}
