from _thread import start_new_thread
from alert import Alert
from client import Client

alert = Alert()
client = Client(alert)

try:
    start_new_thread(alert.run, ())
    start_new_thread(client.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

while True:
    pass



