import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(15, GPIO.OUT)

while 1:
    for row in db(db.waterset.id=='1').select():
        tempsett= row.Water_Temperature
    tempset=float(tempsett)
    text = '';
    while text.split("\n")[0].find("YES") == -1:
        tfile = open("/sys/bus/w1/devices/28-00000457b942/w1_slave")
        text = tfile.read()
        tfile.close()
    tfile = open("/sys/bus/w1/devices/28-00000457b942/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000.0
    temp = round(temperature, 1)
    row = db(db.wtemp.id==1).select().first()
    row.update_record(wtemp=temp)
    db.commit()
    aiml=tempset-0.2
    aimh=tempset+0.2
    if (temp <= aiml):
           GPIO.output(15, GPIO.HIGH)
           heatstat = "ON"
    if (temp >= aimh):
           GPIO.output(15, GPIO.LOW)
           heatstat = "OFF"
    row = db(db.heat.id==1).select().first()
    row.update_record(heat=heatstat)
    time.sleep(1)
