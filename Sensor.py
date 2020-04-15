import time
import colorsys
import Adafruit_ADS1x15
import sys
import Adafruit_DHT
from luma.led_matrix.device import neopixel
from luma.core.legacy import text, show_message
from luma.core.render import canvas
from luma.core.legacy.font import proportional, TINY_FONT

class Sensor:

    def __init__(self):
        print ("Iniciando sensor")
        self.device = neopixel(width=8, height=8)
        self.device.contrast(30)
        self.temp = Adafruit_DHT.DHT11
        self.pin = 4
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1 
        self.DELAY = 5  
 
    def alert(self):
        with canvas(self.device) as draw:
   	        draw.rectangle(self.device.bounding_box, fill="red")
        time.sleep(self.DELAY)
        self.device.clear()

    def message(self,msg):
        color="blue"
        show_message(self.device, msg, y_offset=0, fill=color, font=TINY_FONT,scroll_delay=0.2)
        time.sleep(0.5)
        
    def sensor(self):
        self.sound = self.adc.read_adc(3, gain=self.GAIN)
        self.temperature,self.humidity = Adafruit_DHT.read_retry(self.temp , self.pin)
      
        return self.sound,int(self.temperature), int(self.humidity)


