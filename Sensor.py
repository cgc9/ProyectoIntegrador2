import time
import colorsys
import smbus
import Adafruit_ADS1x15
import sys
import Adafruit_DHT
from luma.led_matrix.device import neopixel
from luma.core.legacy import text, show_message
from luma.core.render import canvas
from luma.core.legacy.font import proportional,TINY_FONT
import  numpy as np

class Sensor:

    def __init__(self):
        print ("Iniciando sensor")
        self.device = neopixel(width=8, height=8)
        self.device.contrast(30)
        self.temp = Adafruit_DHT.DHT11
        self.pin = 17
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1 
        self.DELAY = 5  
        self.DEVICE1= 0x23 # Default device I2C address
        self.POWER_DOWN = 0x00 # No active state
        self.POWER_ON   = 0x01 # Power on
        self.RESET = 0x07 # Reset data register value
        self.ONE_TIME_HIGH_RES_MODE = 0x20
        self.bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
    
    def alert(self):
        msg="SILENCIO"
        with canvas(self.device) as draw:
   	        draw.rectangle(self.device.bounding_box, fill="red")
        time.sleep(self.DELAY)
        show_message(self.device, msg, y_offset=0, fill="white", font=TINY_FONT,scroll_delay=0.2)
        self.device.clear()

    def message(self,msg):
        color="blue"
        show_message(self.device, msg, y_offset=0, fill=color, font=TINY_FONT,scroll_delay=0.2)
        time.sleep(0.5)
        
    def sensor(self):
        cont=0
        total=50
        sounds=[]

        while (cont<total):
            cont=cont+1
            sounds.append(self.adc.read_adc(3))
        
        self.sound = np.mean(sounds)
        self.data = self.bus.read_i2c_block_data(self.DEVICE1,self.ONE_TIME_HIGH_RES_MODE)
        # Simple function to convert 2 bytes of data
        # into a decimal number
        self.light=((self.data[1] + (256 * self.data[0])) / 1.2)
        print("Light: "+ str(self.light))
        self.temperature,self.humidity = Adafruit_DHT.read_retry(self.temp , self.pin)

       
        return int(self.sound),int(self.temperature), int(self.humidity)


