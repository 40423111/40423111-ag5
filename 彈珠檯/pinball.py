import vrep
import keyboard
from time import sleep
import sys, math
# import 需要用到的函式

# //////////////////////////////////////////////
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
# api 與v_rep的通訊協定

if clientID !=-1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
# 檢查是否連接
# ///////////////////////////////////////////////


vel = 270
R_whirl = (math.pi/180)*vel
L_whirl = -(math.pi/180)*vel
# 將速度轉換成角速度

errorCode,ball_handle=vrep.simxGetObjectHandle(clientID,'ball',vrep.simx_opmode_oneshot_wait)
errorCode,move_handle=vrep.simxGetObjectHandle(clientID,'move',vrep.simx_opmode_oneshot_wait)
errorCode,Rrev_handle=vrep.simxGetObjectHandle(clientID,'rev_R',vrep.simx_opmode_oneshot_wait)
errorCode,Lrev_handle=vrep.simxGetObjectHandle(clientID,'rev_L',vrep.simx_opmode_oneshot_wait)
# 設定名稱與v_rep物件連結

if errorCode == -1:
    print('Can not find motor')
    sys.exit()
print(errorCode) # DELETE
# 檢查物件是否連結

def start(): 
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
# 定義函式 start()

def stop():
    errorCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)
# 定義函式 stop()

def pause():
    errorCode = vrep.simxPauseSimulation(clientID,vrep.simx_opmode_oneshot_wait)
# 定義函式 pause()

def button():
    while True:
        try:
            if keyboard.is_pressed('up'):
                vrep.simxSetJointTargetVelocity(clientID,move_handle,-10,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,move_handle,10,vrep.simx_opmode_oneshot_wait)
            # 發球桿控制建(上方向鍵)

            if keyboard.is_pressed('a'):
                vrep.simxSetJointTargetVelocity(clientID,Lrev_handle,R_whirl,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,Lrev_handle,L_whirl,vrep.simx_opmode_oneshot_wait)
            # 右擊球桿控制鍵(a)

            if keyboard.is_pressed('l'):
                vrep.simxSetJointTargetVelocity(clientID,Rrev_handle,L_whirl,vrep.simx_opmode_oneshot_wait)
            else:
                vrep.simxSetJointTargetVelocity(clientID,Rrev_handle,R_whirl,vrep.simx_opmode_oneshot_wait)
            # 右擊球桿控制鍵(a)

        except:
            break
# 定義函式 button()

vrep.simxSetJointTargetVelocity(clientID,Lrev_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,Rrev_handle,0,vrep.simx_opmode_oneshot_wait)
# 設定馬達靜止

start()
button()
stop()
# 呼叫函式