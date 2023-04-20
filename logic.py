# Imports sleep method from system
import sys
from time import sleep

# Imports system from operating system
from os import system

class Logic():
    def __init__(self, isOn):
            self.isOn = isOn

    # Scripts type animation for text when Logic is turned on
    def type(self, text, speed = 0.05):

        if self.isOn:
            string = text
            for char in string:

                sleep(speed)
                sys.stdout.write(char)
                sys.stdout.flush()
        
        else:
            sys.stdout.write(text)
    
    # Scripts blinking animation when Logic is turned on
    def blink(self, dur, trans = 0.0625):

        if self.isOn:
            system("color 0F")
            sleep(dur)
            system("color 80")
            sleep(trans)
            system("color 70")

        else:
            sleep(0.0625)
    
    def next(self):
        self.pause(1)
        self.blink(1)
        system('cls')

    def clear(self):
        system('cls')

    # Scripts a pause
    def pause(self, dur):
        sleep(dur)
    
    # Scripts a system call
    def call(self, prompt):
        system(prompt)