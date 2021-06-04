import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(11, GPIO.IN) 
 
while (True):
    if(GPIO.input(11) == 1):
       GPIO.output(12,0) 
       print("Presença detectada")
    else: 
       GPIO.output(12,1)