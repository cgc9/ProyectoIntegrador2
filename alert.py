from Sensor import Sensor
from publisher import sendData
import  numpy as np
#from publisher import sendData2

import time

class Alert:
    root=None
    def __init__(self):
        self.state = False
        self.sensor=Sensor()
        	      
    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
	
    def run(self):
        ruido = []
        tiempo=0
        contador=0
        num=10
        while True:
            #time.sleep(1)
            if(self.getState()==True):
                #tiempo=tiempo+1
            #if(tiempo<num):
                #print(tiempo)
                #time.sleep(1)
                self.sound, self.tempe,self.humi= self.sensor.sensor()
                self.data="dev1"+"/"+str(self.sound)+"/"+str(self.tempe)+"/"+str(self.humi)+"/"+"32"+"/"+"1"
                print(self.data)
                ruido.append(self.sound)
                print("max: "+str(np.max(ruido))+" Min:"+str(np.min(ruido))+" Mean: "+ str(np.mean(ruido)))

                print(self.data)
                print(self.getState())
                if self.sound >= 1500:
                    contador=contador+1
                    sendData(self.sound,self.tempe,self.humi)
                else:
                    contador=0
                    sendData(self.sound,self.tempe,self.humi)
                print("paso")
            #elif(tiempo==num):
                #tiempo=0
                if(contador>=5):
                    #sendData2(self.sound,self.tempe,self.humi)##Enviar al front
                    self.sensor.alert()
                    print("ALERTAAA")
                    contador=0
                else:
                    print("un no")
                #contador=0
            
            else:
                print("Dispositivo apagado")
			
				 
			  

