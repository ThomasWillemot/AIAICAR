import RPi.GPIO as GPIO
from time import sleep
#AIn1 = 4
#AIn2 = 2
#AIn3 = 17
#AIn4 = 3

LF1 = 6
LF2 = 13
LFen = 27
RF1 = 26
RF2 = 19
RFen = 22



GPIO.setmode(GPIO.BCM)

#GPIO.setup(AIn1,GPIO.OUT)
#GPIO.setup(AIn2,GPIO.OUT)
#GPIO.setup(AIn3,GPIO.OUT)
#GPIO.setup(AIn4,GPIO.OUT)
GPIO.setup(LF1,GPIO.OUT)
GPIO.setup(LF2,GPIO.OUT)
GPIO.setup(RF1,GPIO.OUT)
GPIO.setup(RF2,GPIO.OUT)
GPIO.setup(LFen,GPIO.OUT)
GPIO.setup(RFen,GPIO.OUT)

motor_list = [LF1,LF2,RF1,RF2]#[AIn1,AIn2,AIn3,AIn4,BIn1,BIn2,BIn3,BIn4]

pwmLF=GPIO.PWM(LFen,1000)
pwmRF=GPIO.PWM(RFen,1000)
pwmLF.start(25)
pwmRF.start(25)

#Set all motors off.
for i in range(len(motor_list)):
    GPIO.output(motor_list[i],GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x= input('Command:')
    print(x)
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
        
    elif x=='l':
        print("low")
        pwmLF.ChangeDutyCycle(25)
        pwmRF.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        pwmLF.ChangeDutyCycle(50)
        pwmRF.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pwmLF.ChangeDutyCycle(75)
        pwmRF.ChangeDutyCycle(75)
        x='z'
    elif x=='e':
        GPIO.cleanup()
        break