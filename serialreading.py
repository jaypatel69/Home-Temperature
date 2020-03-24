import serial
import time
import praw
import config

#Logging into Reddit account
try:
    print("Logging into reddit account")
    reddit = praw.Reddit(username=config.username,
                         password=config.password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent="Home Automation using Arduino")
    print("Login Successful")

except Exception as e:
    print("Login Failed")
    print(e)


arduino=serial.Serial("COM8", 9600, timeout=0.1)


#defining a class for reading serial data from arduino
class GetSerialMonitor:
    def __init__(self):
        pass

    def getSerialData(self):
        self.data = arduino.readline()[:-2]
        if self.data:
            self.data=self.data.decode("utf-8")
            self.data=int(self.data)
            print(self.data)
            return self.data

    def closeSerialData(self):
        arduino.close()


#defining an object to read serial data
s=GetSerialMonitor()

#looping over to get serial data from arduino
while True:
    temp=s.getSerialData()
    if temp is None:
        print("No value of temperature found")
    else:
        msg="Temperature of the house is " + str(temp) + "degree  celsius"
        try:
            print("sending PM through Reddit")
            #sending the message
            user="_jaypatel"
            reddit.redditor(user).message("Home Temperature",msg)
            print("message sent successfully")
            exit()
        except Exception as e:
            print("Something went wrong")
            print(e)
