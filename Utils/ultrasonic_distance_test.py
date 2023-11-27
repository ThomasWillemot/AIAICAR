import RPi.GPIO as GPIO
import time
 
LF1 = 6
LF2 = 13
LFen = 27
RF1 = 26
RF2 = 19
RFen = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LF1,GPIO.OUT)
GPIO.setup(LF2,GPIO.OUT)
GPIO.setup(RF1,GPIO.OUT)
GPIO.setup(RF2,GPIO.OUT)
GPIO.setup(LFen,GPIO.OUT)
GPIO.setup(RFen,GPIO.OUT)

motor_list = [LF1,LF2,RF1,RF2]

pwmLF=GPIO.PWM(LFen,1000)
pwmRF=GPIO.PWM(RFen,1000)
pwmLF.start(60)
pwmRF.start(60)


#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 23
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2 /100
 
    return distance
 
def update_pid(distance, integral):
    
    setpoint= 0.5 # distance
    
    error = distance - setpoint
    integral = integral + error
    
    speed = error * 100 + integral * 0.1
    return speed, integral

def stop_motors():
    for i in range(len(motor_list)):
            GPIO.output(motor_list[i],GPIO.LOW)
    

def change_motor_speed(speed, last_direction):
    speed_limited = int(min(speed,100))
    # Forwards               
    if speed > 30:
        print(f'Fw , last was {last_direction}.')
        if last_direction =='fw':
            pwmLF.ChangeDutyCycle(speed_limited)
            pwmRF.ChangeDutyCycle(speed_limited)
        else:
            stop_motors()
            for i in range(len(motor_list)):
                if i%2==0:
                    GPIO.output(motor_list[i],GPIO.HIGH)
        last_direction = 'fw'
            
    # Backwards
    elif speed < -30:
        if last_direction =='bw':
                    pwmLF.ChangeDutyCycle(-speed_limited)
                    pwmRF.ChangeDutyCycle(-speed_limited)
        else:
            stop_motors()
            for i in range(len(motor_list)):
                if i%2==1:
                    GPIO.output(motor_list[i],GPIO.HIGH)
        last_direction = 'bw'
        
    
    else:
        last_direction = 'stop'
        pwmLF.ChangeDutyCycle(0)
        pwmRF.ChangeDutyCycle(0)
    return last_direction

if __name__ == '__main__':
    try:
        for i in range(len(motor_list)):
            if i%2==0:
                GPIO.output(motor_list[i],GPIO.HIGH)
        integral = 0
        time.sleep(0.5)
        print('Motors running')
        running=True
        last_direction = 'fw'
        while running:
            
            dist = distance()
            print ("Measured Distance = %.1f m" % dist)
            speed, integral = update_pid(dist, integral)
            print(f"Control action: {speed}, integral {integral}")
            last_direction = change_motor_speed(speed, last_direction)
            
            time.sleep(0.5)
        print('Stopping motors')
        stop_motors()
        time.sleep(2)
        GPIO.cleanup()
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Stopped by User")
        GPIO.cleanup()