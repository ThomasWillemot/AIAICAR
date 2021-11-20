"""
Driving functions, should contain forward, backward, turning and driving turns in all directions.
"""


class CarControls:
    def __init__(self,config_ports):
        # Stands for [position left/right][position front/rear][forward/backward]
            LFF = config_ports[0]
            LFB = config_ports[1]
            LRF = config_ports[2]
            LRB = config_ports[3]
            RFF = config_ports[4]
            RFB = config_ports[5]
            RRF = config_ports[6]
            RRB = config_ports[7]

    def stop(self):
        return True

    def drive_forward(self):
        return False

    def drive_backward(self):
        return False

    def rotate_left(self):
        return False

    def rotate_right(self):
        return False

    def drive_front_left(self):
        return False

    def drive_front_right(self):
        return False

    def drive_back_left(self):
        return False

    def drive_back_right(self):
        return False