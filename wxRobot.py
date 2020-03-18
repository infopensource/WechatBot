import msgDB
import _thread
import requests
import urllib3
import random
import time
import sys
import os

urllib3.disable_warnings()

def rest_program():
    print('restart')
    #python = sys.executable
    #os.execl(python, python, * sys.argv)
    #return "a"

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def local_picture(name):
      img_url ='https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php'
      img = requests.get(img_url,verify=False) 
      f = open('C:\\pic\\'+str(name)+'.jpg','ab') #存储图片，多媒体文件需要参数b（二进制文件）
      f.write(img.content) #多媒体存储content
      f.close()

def out():
    time.sleep(36000)
    

msgDB.initDB()
msgDB.delMsg()
#_thread.start_new_thread(out,())

#for i in range(1000):#清除所有未处理消息
#    msgDB.delMsg()

for i in range(1000):
    try:
        res=msgDB.listen_wxMsg()

        if res==False:#未监听到消息
            continue
        
        if res[3]=="菜单":
            print(res[0])
            msgDB.send_wxMsg(res[0],'''功能列表：
            1.汤圆刷数据
            2.小姐姐连抽
            3.待开发''')
            msgDB.delMsg()
            continue

        if res[3].split()[0]=="小姐姐连抽":
            print(res[0])
            
            if len(res[3].split())!=2 or is_int(res[3].split()[1])==False:
                msgDB.send_wxMsg(res[0],"参数错误")
                msgDB.delMsg()
                continue
            
            for i in range(int(res[3].split()[1])):
                local_picture("test")
                msgDB.send_wxPicture(res[0],"C:\\pic\\"+str(random.randint(0,1000))+".jpg")
                #msgDB.send_wxPicture(res[0],"C:\\1.jpg")
                msgDB.delMsg()
                continue

        if res[3]=="debug":
            msgDB.delMsg()
            continue

        if res[3]=="rst":
            exit()
            continue

        msgDB.delMsg()
    except:
        print("error")
        #msgDB.delMsg()
        #msgDB.endDb()
        #msgDB.initDB()
        exit()
