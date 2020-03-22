///*************************************************** 
//  Copied from an Adafruit library for porting to the Raspberry Pi
//  
//  This is a library for the MLX90614 Temp Sensor
//
//  Designed specifically to work with the MLX90614 sensors in the
//  adafruit shop
//  ----> https://www.adafruit.com/products/1748
//  ----> https://www.adafruit.com/products/1749
//
//  These sensors use I2C to communicate, 2 pins are required to  
//  interface
//  Adafruit invests time and resources providing this open source code, 
//  please support Adafruit and open-source hardware by purchasing 
//  products from Adafruit!
//
//  Written by Limor Fried/Ladyada for Adafruit Industries.  
//  BSD license, all text above must be included in any redistribution
// ****************************************************/
//
#include <Wire.h>
#if (ARDUINO >= 100)
 #include "Arduino.h"
#else
 #include "WProgram.h"
#endif

#define MLX90614_ADDR 0x5A
// RAM
#define MLX90614_RAWIR1 0x04
#define MLX90614_RAWIR2 0x05
#define MLX90614_TA 0x06
#define MLX90614_TOBJ1 0x07
#define MLX90614_TOBJ2 0x08
// EEPROM
#define MLX90614_TOMAX 0x20
#define MLX90614_TOMIN 0x21
#define MLX90614_PWMCTRL 0x22
#define MLX90614_TARANGE 0x23
#define MLX90614_EMISS 0x24
#define MLX90614_CONFIG 0x25
#define MLX90614_ADDR 0x0E
#define MLX90614_ID1 0x3C
#define MLX90614_ID2 0x3D
#define MLX90614_ID3 0x3E
#define MLX90614_ID4 0x3F

uint8_t mlxAddr = MLX90614_ADDR;

float readTempC(uint8_t reg)
{
  float temp = readShort(reg);
  temp = temp*0.02 - 273.15;
  return temp;
}

uint16_t readShort(uint8_t reg)
{
  // TODO: do we want the PEC?
  uint16_t h;

  Wire.beginTransmission((uint8_t)0x5A);
  Wire.write(reg);
  Wire.endTransmission(false);

  Wire.requestFrom((uint8_t)0x5A, (uint8_t)3);
  h = Wire.read();
  h |= Wire.read() << 8;

  uint8_t pec = Wire.read();
  //Serial.println(pec);
  return h;
}

unsigned long int milli_time;
float temp1;
float temp2;
float ambientTemp;
float angle_pan; // from servo 1
float angle_tilt; // from servo 2

void setup() {
  Serial.begin(115200);
  Wire.begin();
  delay(100);
  while (!Serial);
  Serial.println("CLEARDATA");
  Serial.println("LABEL,Computer Time,Sensor Time,Ambient Temperature, Temp1, Temp2, Pan Angle, Tilt Angle");
}

void loop() {
  // read the ambient and object temperatures
  float ambTemp = readTempC(MLX90614_TA);
  float objTemp1 = readTempC(MLX90614_TOBJ1);
  float objTemp2 = readTempC(MLX90614_TOBJ2);

  // change the servo motor and store the anngles
  // angle_pan = ??, Servo.????
  // angle_tilt = ??, Servo.????

  milli_time = millis();
    
  //Sensor Time,Ambient Temperature, Temp1, Temp2, Pan Angle, Tilt Angle

  Serial.print("DATA,TIME,"); // begin data, took care of `Computer Time` at beginning
  Serial.print(milli_time); // Sensor Time
  Serial.print(",");
  Serial.print(ambTemp); // Ambient temp
  Serial.print(",");
  Serial.print(objTemp1); // Temp1
  Serial.print(",");
  Serial.print(objTemp2); // Temp2
  Serial.print(",");
  Serial.print(angle_pan); // Pan Angle
  Serial.print(",");
  Serial.print(angle_tilt); // Tilt Angle
  Serial.println(); // END-OF-LINE to register datapoint
  delay(100); // Wait for the serial to push everything out 
}
