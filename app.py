import time
import RPi.GPIO as GPIO
import urllib
import urllib.request
import json
import requests

API = "https://api.thingspeak.com/update?api_key=YOUR_API_KEY"

#TO get the distance from the sensor

def getSensorData():
    GPIO.setmode(GPIO.BOARD)
    trig = 38  # sends the signal
    echo = 40  # listens for the signal
    GPIO.setwarnings(False)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0: pass

    start = time.time()  # reached when echo listens

    while GPIO.input(echo) == 1:  pass

    end = time.time() # reached when signal arrived

    distance = ((end - start) * 34300) / 2

    return (int (distance))


def cloudData():
    print ('starting...')       
    while True:
        distance = cloudData()
        Header = "&field1={}".format(distance)
        newurl=API+Header
        print (newurl)
        data = urllib.request.urlopen(newurl)
        print (data)
        time.sleep(1)
        f.close()

            
# call main
if __name__ == '__main__':
    cloudData()
    GPIO.cleanup()
    print ('exiting.')
    exit()