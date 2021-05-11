"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt


# this is the function for all the text and has a parameter of clueValue
def display_text(clueValue):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*(clueValue["clueSlider/accelXRange"], clueValue["clueSlider/accelYRange"], clueValue["clueSlider/accelZRange"]))#thi is for acceleration, passing the topic in clueValue parameter
    clue_data[1].text = "Gyro: {} {} {} dps".format(*(clueValue["clueSlider/gyroXRange"], clueValue["clueSlider/gyroYRange"], clueValue["clueSlider/gyroZRange"]))
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*(clueValue["clueSlider/magneticXRange"], clueValue["clueSlider/magneticYRange"], clueValue["clueSlider/magneticZRange"]))
    clue_data[3].text = "Pressure: {} hPa".format(clueValue["clueSlider/pressureRange"])
    clue_data[4].text = "Temperature: {} C".format(clueValue["clueSlider/tempRange"])
    clue_data[5].text = "Humidity: {} %".format(clueValue["clueSlider/humidityRange"])
    clue_data[6].text = "Proximity: {}".format(clueValue["clueSlider/proximityRange"])
    clue_data[7].text = "Color: R:{}G:{}B:{}C:{}".format(*(clueValue["clueSlider/colorRRange"], clueValue["clueSlider/colorGRange"], clueValue["clueSlider/colorBRange"], clueValue["clueSlider/colorCRange"]))
    clue_data.show()
    
#declare a variable clueData wherein
#put all the topic of the clueSlider
clueData = {
    "clueSlider/accelXRange" : 0,
    "clueSlider/accelYRange" : 0,
    "clueSlider/accelZRange" : 0,
    "clueSlider/gyroXRange" : 0,
    "clueSlider/gyroYRange" : 0,
    "clueSlider/gyroZRange" : 0,
    "clueSlider/magneticXRange" : 0,
    "clueSlider/magneticYRange" : 0,
    "clueSlider/magneticZRange" : 0,
    "clueSlider/pressureRange" : 800,
    "clueSlider/tempRange" : clue.temperature,
    "clueSlider/humidityRange" : clue.humidity,
    "clueSlider/proximityRange" : clue.proximity,
    "clueSlider/colorRRange" : 0,
    "clueSlider/colorGRange" : 0,
    "clueSlider/colorBRange" : 0,
    "clueSlider/colorCRange" : 0
}

def on_connect(client, userdata, flags, rc):
    if rc == 0: #if the return code is == 0 
        client.subscribe("clueSlider/#") #client.subscribe to the topic in a wildcard, it will only read the clueslider and the rest will ignore bec. of the hashtag symbol that means the mullti-level wildcard in the topic
        display_text(clueData) #passes the argument clueData in the display_text() function

def on_message(client, userdata, msg):
    clueData[msg.topic]= msg.payload.decode() #if the topic is equal to payload
    display_text(clueData) #display the value of specific components 

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()