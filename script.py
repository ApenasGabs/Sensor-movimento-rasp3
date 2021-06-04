import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
print("Rodando script") 
while (True):
    if(GPIO.input(13) == 1):
        GPIO.output(11, 0)
        print("Presença detectada")
    else:
        GPIO.output(11, 1)
