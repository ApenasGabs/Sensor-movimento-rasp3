import RPi.GPIO as GPIO
from time import *
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT) 
print("Rodando script")
X = int(input("Digite o numero de vezes: "))
while ( X > 0):#GPIO.input(11) == 1
    X = X - 1
    sleep(1)
    print("liga ")
    GPIO.output(11,0)
    sleep(1)
    GPIO.output(11,1)
    print("desliga ") 
