import time
import colorsys
from luma.led_matrix.device import neopixel
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, TINY_FONT
from alert import Alert
from Sensor import Sensor
import paho.mqtt.client as mqtt


MQTT_REMOTE_SERVER="192.168.1.8"
#MQTT_REMOTE_SERVER="chimpanzee.rmq.cloudamqp.com"
MQTT_PATH_RECV="iot"
#USER="qeqwzcps:qeqwzcps"
#PASS="ijOv0DHpdzRleeN0_axHnaSEk5HLlVmt"
USER="iotbroker"
PASS="iotbroker"

class Client:
    
    def __init__(self,alert):
        self.sensor=Sensor()
        self.alert = alert
        self.flag = True
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(USER,PASS)
        self.client.connect(MQTT_REMOTE_SERVER,1883,60)
        print("connected")

    def on_connect(self, client, userdata, flags, rc):
        print("External Comm: connected with result code " + str(rc))
        client.subscribe(MQTT_PATH_RECV)


    def start(self):
        print("looping")
        self.client.loop_forever()
       

    def on_message(self, client, userdata, msg):
        mensaje=str(msg.payload).split('b')[1]
        print('payload:'+ mensaje)
        if(mensaje == "'-99'"):
            self.alert.setState(True)
            print("Iniciando")
        elif(mensaje=="'-100'"):
            self.alert.setState(False)
            print("Finalizando")
        else:
            if(self.alert.getState()==False):
                print('Encienda el dispositivo para enviar mensajes')
            else:
                self.sensor.message(mensaje)
               
                


	

  


       
   





 
    



	

  


       
   





 
    



  


	

  


       
   





 
    

