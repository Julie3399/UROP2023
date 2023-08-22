from mistyPy import Robot
from mistyPy import IdeComm

comm = IdeComm()

def speaking_test():
    comm.send_message('starting')
    misty = Robot("192.168.0.101")
    misty.speak("Hello, world!")
    #Your code here

    comm.shutdown()

if __name__ == '__main__':
    misty_ip = "192.168.0.101"
    misty = Robot(misty_ip)
    comm.start(speaking_test)