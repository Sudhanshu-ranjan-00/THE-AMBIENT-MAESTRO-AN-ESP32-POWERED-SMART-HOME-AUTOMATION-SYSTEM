from machine import Pin, PWM
from servo import Servo
import dht
import time

# Define pin connections
ldr_pin = 34
dht_pin = 26
servo_pin = 14
led_pin = 2
ac_led_pin = 4
enable_pin = 23
input1_pin = 22
input2_pin = 21
pir_pin = 5
fan_pin = 12  # Example pin for fan control

# Initialize components
ldr = Pin(ldr_pin, Pin.IN)
dht_sensor = dht.DHT11(Pin(dht_pin))
servo = Servo(pin = 14)
led = Pin(led_pin, Pin.OUT)
ac_led = Pin(ac_led_pin, Pin.OUT)
motor_enable = Pin(enable_pin, Pin.OUT)
motor_input1 = Pin(input1_pin, Pin.OUT)
motor_input2 = Pin(input2_pin, Pin.OUT)
pir = Pin(pir_pin, Pin.IN)
fan_pwm = PWM(Pin(fan_pin), freq=1000, duty=0)  # Initialize fan PWM

# Define motor control functions
def motor_forward():
    motor_input1.on()
    motor_input2.off()

def motor_backward():
    motor_input1.off()
    motor_input2.on()

def motor_stop():
    motor_input1.off()
    motor_input2.off()

# Initialize variables
motion_detected = False
person_in_room = False

# Main loop
while True:
    if pir.value() == 1:
        if not motion_detected:
            motion_detected = True
            if not person_in_room:
                print("Person enters the room.")
                person_in_room = True
            else:
                print("Person leaves the room.")
                person_in_room = False
        else:
            motion_detected = False

    if person_in_room:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        light_percentage = (ldr.value() / 4095) * 100  # Assuming 12-bit ADC

        print("Temperature:", temperature, "C")
        print("Light percentage:", light_percentage)

        if temperature < 24:
            motor_enable.on()
            motor_forward()
            servo.move(0)
            fan_pwm.duty(102)  # 10% duty cycle for 10% speed
            print("Fan speed adjusted to 10%")
        elif 24 <= temperature <= 30:
            motor_enable.on()
            motor_backward()
            servo.move(90)
            fan_pwm.duty(512)  # 50% duty cycle for 50% speed
            print("Fan speed adjusted to 50%")
        else:
            motor_enable.on()
            motor_backward()
            servo.move(180)
            fan_pwm.duty(1023)  # Full speed
            print("Fan speed adjusted to 100%")

        if light_percentage > 50:  # Assuming 50% as threshold for daytime
            led.off()
            print("LED turned off")
        else:
            led.on()
            print("LED turned on")

        if temperature > 32:
            ac_led.on()
            print("AC turned on")
        else:
            ac_led.off()
            print("AC turned off")

    else:
        motor_enable.off()
        motor_stop()
        servo.move(0)
        led.off()
        ac_led.off()
        fan_pwm.duty(0)  # Turn off fan
        print("Fan turned off")

    time.sleep(1)  # Adjust sleep time as needed

