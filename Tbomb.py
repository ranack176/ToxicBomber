#########################################
# ToxicBomber
# A Bangladeshi SMS and Call Bomber Tool
# Author: ToxicNoob Inc.
# GitHub: https://github.com/Toxic-Noob
# Version: 5.0.0
#########################################

import time
import random
import os
import shutil
import sys

# Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 11):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not Supported!")
        print("[\033[92m*\033[37m] Update Your Python Using the Command Below:\n\n    pkg reinstall python\n")
        sys.exit()

def showAuthorMsg(msg):
    print()
    print("\033[94m-"*columns, end="")
    print("\033[92mMessage From Author".center(columns+4))
    print("\033[95m-"*columns, end="")
    psb("\n\033[37m    " + msg + "\n")
    print("\033[94m-"*columns, end="", flush=1)
    print()
    open("./more/.msg", "w").write(msg)
    time.sleep(1)
    input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
    logo()

def update():
    try:
        toolVersion = json.loads(open("./more/.version", "r").read())["version"]
    except:
        toolVersion = "ToxicNoob"
    
    try:
        authorMsg = open("./more/.msg", "r").read().replace("\n", "")
    except:
        authorMsg = "None"
    
    try:
        parsedData = requests.get("https://raw.githubusercontent.com/Toxic-Noob/ToxicBomber/main/more/.version").json()
    except:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Connect To The Internet!")
        time.sleep(1)
        l = input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
        update()
    
    mainVersion = parsedData["version"]
    newMsg = parsedData["message"]
    
    if (toolVersion != mainVersion):
        psb("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
        time.sleep(0.5)
        psb("    \033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")
        
        os.system("cd .. && rm -rf ToxicBomber && git clone https://github.com/Toxic-Noob/ToxicBomber > /dev/null 2>&1")
        
        print("\033[37mDone")
        psb("\n    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
        time.sleep(0.8)
        
        os.system("cd .. && cd ToxicBomber && python Tbomb.py")
    
    else:
        if (authorMsg != newMsg) and (newMsg != "blank"):
            showAuthorMsg(newMsg)

def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│     \033[92m▀▛▘     ▗    ▛▀▖       ▌        \033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▌▞▀▖▚▗▘▄ ▞▀▖▙▄▘▞▀▖▛▚▀▖▛▀▖▞▀▖▙▀▖\033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▌▌ ▌▗▚ ▐ ▌ ▖▌ ▌▌ ▌▌▐ ▌▌ ▌▛▀ ▌  \033[94m   │".center(columns+15))
    print("\033[94m│     \033[92m ▘▝▀ ▘ ▘▀▘▝▀ ▀▀ ▝▀ ▘▝ ▘▀▀ ▝▀▘▘  \033[94m   │".center(columns+15))
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor : ToxicNoob Inc.                \033[94m│".center(columns+15))
    print("│ \033[95mTool   : SMS and Call Bomber           \033[94m│".center(columns+9))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns+9))
    print("│ \033[95mCoder  : HunterSl4d3              \033[37mV5.0 \033[94m│".center(columns+15))
    print("\033[94m└────────────────────────────────────────┘".center(columns+5))

def banner():
    global number, amount, delay
    amount_str = str(amount)
    amount_str = amount_str + (" " * (21-len(amount_str)))
    
    print("\033[95m-" * (columns), end="")
    print(("\033[92mTarget  : \033[37m0" + number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount_str).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * (columns), end="")
    print("\n")

def check(sent):
    global amount
    delay = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Delay Between SMS (in seconds):> \033[37m"))
    
    localTime = time.localtime()
    current_time = time.strftime("%I:%M:%S", localTime)

    print(f"\r\033[92m    [\033[94m {current_time} \033[92m] Message Sent : \033[94m[\033[37m{sent}\033[94m]\033[37m", end="")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        return True
    else:
        time.sleep(delay)
        return False

def getNumber():
    number = input("\n    \033[92m[\033[37m*\033
def getNumber():
    number = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target (\033[92mWithout +88\033[37m):> \033[37m")
    if not number.isdigit():
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        return getNumber()
    if not (len(number) == 11):
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")
        return getNumber()
    
    return number

def call_bombing_process():
    global number, amount
    number = getNumber()
    amount = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount of Calls to Make:> \033[37m"))
    banner()
    
    sent_calls = 0
    while sent_calls < amount:
        if call_bomb(number):
            sent_calls += 1
        check(sent_calls)

def sms_bombing_process():
    global number, amount
    number = getNumber()
    amount = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount of SMS to Send:> \033[37m"))
    delay = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Delay Between SMS (in seconds):> \033[37m"))
    banner()
    
    sent_sms = 0
    while sent_sms < amount:
        # Simulate sending an SMS
        psb(f"\nSimulating SMS to {number}...")
        time.sleep(delay)  # Simulate delay between SMS
        sent_sms += 1
        check(sent_sms)

def main_menu():
    global number, amount
    os.system("clear")
    logo()
    print("\n    \033[92m[\033[37m*\033[92m] \033[37mSelect the type of bombing:")
    print("    \033[92m[\033[37m1\033[92m] \033[37mSMS Bombing")
    print("    \033[92m[\033[37m2\033[92m] \033[37mCall Bombing")
    choice = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter your choice (1 or 2):> \033[37m")

    if choice == '1':
        sms_bombing_process()
    elif choice == '2':
        call_bombing_process()
    else:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mInvalid Choice! Exiting...")
        sys.exit()

if __name__ == "__main__":
    checkPy()
    update()
    main_menu()
