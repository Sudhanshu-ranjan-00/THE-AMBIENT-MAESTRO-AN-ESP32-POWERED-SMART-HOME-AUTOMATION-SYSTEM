# THE-AMBIENT-MAESTRO-AN-ESP32-POWERED-SMART-HOME-AUTOMATION-SYSTEM
We've designed an esp32 micropython based home automation system that is cost-efficient, energy-efficient, will provide the maximum comfort to the user.
The project contains an esp32, a servo motor attached with a gear based rod, a dht11 sensor, a pir sensor, a dc motor, a led to represent A.C., a photoregister, another led to represent led bulb of the room.
Basically, first we're testing whether there exist a person in the room by using pir sensor, if the person exist, we'll be checking the temperature of the room, if the temperature goes beyond a certain degree, the height of the fan is adjusted automatically to the down and also the speed of the fan is increased, another case will be if the temperature is below a certain degree, the height of the fan is minimized and the speed of the fan is decreased giving the user maximum comfort. 
In the presence of person in the room, we're testing the light intensity, if the percentage of light is above a certain number, the led bulb is automatically getting turned off. else the light will be turned on.
We've also implemented iot cloud platform blynk, that's helping us in turning on or off the led that represents the A.C. remotely.
