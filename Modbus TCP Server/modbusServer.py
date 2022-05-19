from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import socket
import psycopg2
import datetime


server = ModbusServer("192.168.1.150", 8000, no_block = True) # make hostIp your local machine ip

conn = psycopg2.connect(
   database="d7m1sonboebnpr", 
   user='gppafqfrzgxajy', 
   password='156653557573226c1688f8ec9587f3f64f7831bbc5904c60fd65d99eaba57bd7', 
   host='ec2-34-246-227-219.eu-west-1.compute.amazonaws.com', 
   port= '5432'
)
cur = conn.cursor()

try:
    print("Start server...")
    server.start()
    print("Server is online")
    print("Local IP: " + socket.gethostbyname(socket.gethostname()))
    temperature = DataBank.get_words(100)[0]
    brightStatus = DataBank.get_words(500)[0]
    i = 0
    while True:
        newTemperature = DataBank.get_words(100)[0]
        newBrightStatus = DataBank.get_words(500)[0]

        if(temperature != newTemperature and temperature != 65535):
            temperature = newTemperature
            ts = datetime.datetime.now()
            cur.execute("INSERT INTO tbl_sr_temperature_info(temperature, temperature_date) VALUES (%s, %s)", (temperature, ts,))
            conn.commit()
        
        if(brightStatus != newBrightStatus and brightStatus != 65535):
            brightStatus = newBrightStatus
            ts = datetime.datetime.now()
            if brightStatus == 1: # means door closed
                print("Door Closed")
                cur.execute("INSERT INTO tbl_sr_door_status_info(is_door_opened, status_date) VALUES (False, %s)", (ts,))
            elif brightStatus == 0:# means door opened
                print("Door Opened")
                cur.execute("INSERT INTO tbl_sr_door_status_info(is_door_opened, status_date) VALUES (True, %s)", (ts,))
            conn.commit()

        print(str(i) + " Time, Temperature: " + str(temperature) + " BrightStatus: " + str(brightStatus))
        i+=1
        sleep(0.5)
except Exception as E:
    print("Shutdown server...")
    print(E)
    server.stop()
    print("Server is offline")