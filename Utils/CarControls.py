"""
Driving functions, should contain forward, backward, turning and driving turns in all directions.
"""
import RPi.GPIO as GPIO

class CarControls:
    def __init__(self,config_ports):
        # Stands for [position left/right][position front/rear][forward/backward]
        self.config_ports = config_ports
        GPIO.setmode(GPIO.BCM)
        for port in self.config_ports:
            GPIO.setup(port, GPIO.OUT)

    def stop(self):
        for port in self.config_ports:
            GPIO.output(port, GPIO.LOW)
        return True

    def drive_forward(self):
        for i in range(len(self.config_ports)):
            if i % 2 == 0:
                GPIO.output(self.config_ports[i], GPIO.HIGH)
            else:
                GPIO.output(self.config_ports[i], GPIO.LOW)

    def drive_backward(self):
        for i in range(len(self.config_ports)):
            if i % 2 == 1:
                GPIO.output(self.config_ports[i], GPIO.HIGH)
            else:
                GPIO.output(self.config_ports[i], GPIO.LOW)


    def exit_drive(self):
        GPIO.cleanup()

    def rotate_left(self):
        high_ports = [1, 2, 5, 6]
        for i in range(len(self.config_ports)):
            if i in high_ports:
                GPIO.output(self.config_ports[i], GPIO.HIGH)
            else:
                GPIO.output(self.config_ports[i], GPIO.LOW)

    def rotate_right(self):
        high_ports = [0, 3, 4, 7]
        for i in range(len(self.config_ports)):
            if i in high_ports:
                GPIO.output(self.config_ports[i], GPIO.HIGH)
            else:
                GPIO.output(self.config_ports[i], GPIO.LOW)

    def drive_front_left(self):
        return False

    def drive_front_right(self):
        return False

    def drive_back_left(self):
        return False

    def drive_back_right(self):
        return False

