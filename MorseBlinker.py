import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

hello = "Hello World"

morse_library = {
    'H': '....',
    'E': '.',
    'L': '.-..',
    'O': '---',
    'W': '.--',
    'R': '.-.',
    'D': '-..',
}

def write_GPIO(channel, value, sleep_time):
    GPIO.output(channel, value)
    time.sleep(sleep_time)
    # print("GPIO value is {}, time sleep is {}".format(value, sleep_time))
    # To test w/o Raspberry Pi and breadboard, comment out GPIO and uncomment print statement
    

def dot(): # 1 unit
    write_GPIO(11, True, 1)


def dash(): # 3 units
    write_GPIO(11, True, 3)


def space_1(): # Space between portions of same letter
    write_GPIO(11, False, 1)


def space_3(): # Space between two letters
    write_GPIO(11, False, 2) # Adds to 3 unit pause when coupled with space_1


def space_7(): # Space between two words
    write_GPIO(11, False, 4) # Adds to 7 unit pause when coupled with space_1 and space_3
    

for word in hello.split(" "):
    for char in word:
        for symbol in morse_library[char.upper()]:
            if symbol == ".":
                dot()
            elif symbol == "-":
                dash()
            space_1()
        space_3()
    space_7()
    
