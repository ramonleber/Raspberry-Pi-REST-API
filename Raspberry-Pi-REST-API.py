#!/usr/bin/python3

import threading
import time
import os
from pyautogui import press, typewrite, hotkey
from flask import Flask
app = Flask(__name__)
start_only_execute_once = True
stop_only_execute_once = True

def start( threadName ):
    print("Thread1")a
    os.system('sudo python test.py Led')
    time.sleep(4)
    os.system('sudo python Line_Tracking.py')

def stop( threadName ):
    print("Thread2")
    time.sleep(30)
    hotkey('ctrl', 'c')

@app.route('/', methods=["GET"])
def index():
    global start_only_execute_once
    global stop_only_execute_once
    try:
        thread1 = threading.Thread(target=start, args=(1,))
        thread2 = threading.Thread(target=stop, args=(1,))
    except:
        print ("Error: unable to start thread")
    if start_only_execute_once:
        start_only_execute_once = False
        thread1.start()
    if stop_only_execute_once:
        stop_only_execute_once = False
        thread2.start()
    return "Send car comand received"
app.run(debug=True, host='hostname', port='port')
