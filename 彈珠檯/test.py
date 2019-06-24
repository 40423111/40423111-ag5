import vrep
import keyboard
from time import sleep
import sys, math

# //////////////////////////////////////////////
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID !=-1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
# ///////////////////////////////////////////////

KickBallV = 270
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
Move_Minus =-0.1        
Move_Plus =0.1
n=1

errorCode,re_handle=vrep.simxGetObjectHandle(clientID,'re',vrep.simx_opmode_oneshot_wait)
errorCode,cr_handle=vrep.simxGetObjectHandle(clientID,'cy',vrep.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
print(errorCode) # DELETE

def start(): 
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def stop():
    errorCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def pause():
    errorCode = vrep.simxPauseSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def getballposition():
    while True:
        try:
            if keyboard.is_pressed('a'):
                vrep.simxSetJointTargetVelocity(clientID,re_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            else:
                pass
        except:
            break

vrep.simxSetJointTargetVelocity(clientID,re_handle,0,vrep.simx_opmode_oneshot_wait)

start()
getballposition()