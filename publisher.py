import paho.mqtt.publish as publish
import time

MQTT_REMOTE_SERVER="192.168.1.8"
#MQTT_REMOTE_SERVER="chimpanzee.rmq.cloudamqp.com"
MQTT_PATH_SEND= "iotSound"
USER="iotbroker"
PASS="iotbroker"
#USER="qeqwzcps:qeqwzcps"
#PASS="ijOv0DHpdzRleeN0_axHnaSEk5HLlVmt"

ahora = time.strftime("%c")

def sendData(sound,temp,humidity):
    value="dev1/"+str(sound)+"/"+str(int(temp))+"/"+str(int(humidity))+"/42"+"/0"
    try:
	
        publish.single(MQTT_PATH_SEND, value, hostname= MQTT_REMOTE_SERVER,
                       auth={'username':USER,'password':PASS})
        
    except Exception as ex:
        print("Error in sendSound(). ex: {}".format(ex))

def sendSound2(sound):#Para enviar alerta al front, cambiar User, pass... etc
    try:
        publish.single(MQTT_PATH_SEND, "c"+str(sound), hostname= MQTT_REMOTE_SERVER,
                       auth={'username':USER,'password':PASS})
        
    except Exception as ex:
        print("Error in sendSound(). ex: {}".format(ex))

        
    



 
    

        
    



 
    
