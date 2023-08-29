import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()
red = board.get_pin('d:11:o')
yellow = board.get_pin('d:12:o')
green = board.get_pin('d:13:o')

def RedToGreen(wait_yellow):
    red.write(0)
    yellow.write(1)
    time.sleep(wait_yellow)
    yellow.write(0)
    green.write(1)

def GreenToRed(wait_yellow):
    green.write(0)
    yellow.write(1)
    time.sleep(wait_yellow)
    yellow.write(0)
    red.write(1)

def main():
    pass

