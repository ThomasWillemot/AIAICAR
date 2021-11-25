import RPi.GPIO as GPIO
from time import sleep
AIn1 = 4
AIn2 = 2
AIn3 = 17
AIn4 = 3

BIn1 = 6
BIn2 = 13
BIn3 = 19
BIn4 = 26



GPIO.setmode(GPIO.BCM)

GPIO.setup(AIn1,GPIO.OUT)
GPIO.setup(AIn2,GPIO.OUT)
GPIO.setup(AIn3,GPIO.OUT)
GPIO.setup(AIn4,GPIO.OUT)
GPIO.setup(BIn1,GPIO.OUT)
GPIO.setup(BIn2,GPIO.OUT)
GPIO.setup(BIn3,GPIO.OUT)
GPIO.setup(BIn4,GPIO.OUT)

motor_list = [AIn1,AIn2,AIn3,AIn4,BIn1,BIn2,BIn3,BIn4]

#Set all motors off.
for i in range(len(motor_list)):
    GPIO.output(motor_list[i],GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x= input('Command:').split()
    
    if x=='f':
        print("forward")
        for i in range(len(motor_list)):
            if i%2==0:
                GPIO.output(motor_list[i],GPIO.HIGH)
        x = 'z'
    elif x=='s':
        print("stop")
        for i in range(len(motor_list)):
            GPIO.output(motor_list[i],GPIO.LOW)
        x='z'

    elif x=='b':
        for i in range(len(motor_list)):
            if i%2==1:
                GPIO.output(motor_list[i],GPIO.HIGH)
        x = 'z'
    elif x=='e':
        GPIO.cleanup()
        break