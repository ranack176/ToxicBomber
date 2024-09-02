#########################################
# ToxicBomber
# A Bangladeshi SMS and Call Bomber Tool
# Author: ToxicNoob Inc.
# GitHub: https://github.com/Toxic-Noob
# Version: 5.0.0
#########################################

import time
import requests
import sys
import os
import shutil
import json

# Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# Check Python Version, as Python < 3.11 Does not support 3.11 encryption
def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 11):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not Supported!")
        print("[\033[92m*\033[37m] Update Your Python Using the Command Below:\n\n    pkg reinstall python\n")
        sys.exit()

# Show New Message from Author
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

# Check Update
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
    
    # If Tool Version Is not Same, Update Tool
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

# Logo
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


# Options Banner
def banner():
    amount = str(main.amount)
    # 21 - 1(lenOfAmount) = 20....
    amount = amount + (" " * (21-len(amount)))
    
    print("\033[95m-" * (columns), end = "")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * (columns), end = "")
    print("\n")

# Check SMS Sent and Process
def check(sent):
    amount = main.amount
    delay = main.delay
    
    localTime = time.localtime()
    current_time = time.strftime("%I:%M:%S", localTime)

    print(f"\r\033[92m    [\033[94m {current_time} \033[92m] Message Sent : \033[94m[\033[37m{sent}\033[94m]\033[37m", end="")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        
        return True
    else:
        time.sleep(delay)
        return False

# Get Target Number
def getNumber():
    num = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target (\033[92mWithout +88\033[37m):> \033[37m")
    if not num.isdigit():
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        num = getNumber()
    if not (len(num) == 11):
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")
        num = getNumber()
    
    return num

# Function for Call Bombing
def call_bomb(number):
    try:
        response = requests.post(
            "https://api.callservice.com/v1/call",
            headers={"Authorization": "Bearer YOUR_API_KEY"},
            json={"to": number, "from": "YOUR_NUMBER", "message": "This is a call bomb!"}
        )
        if response.status_code == 200:
            print(f"Call to {number} sent successfully.")
            return True
        else:
            print(f"Failed to send call to {number}. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Function for SMS Bombing
def sms_bomb(number, amount):
    for i in range(amount):
        try:
            response = requests.post(
                "https://api.smsservice.com/v1/send",
                headers={"Authorization": "Bearer YOUR_API_KEY"},
                json={"to": number, "message": "This is an SMS bomb!"}
            )
            if response.status_code == 200:
                print(f"SMS sent to {number}.")
            else:
                print(f"Failed to send SMS to {number}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(1)  # Delay between messages

# Main Menu
def main_menu():
    os.system("clear")
    print("\033[94m┌─────────────────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│ \033[92mWelcome to ToxicBomber v5.0.0                        \033[94m│".center(columns+5))
    print("\033[94m│ \033[92mSelect the Bombing Type:                            \033[94m│".center(columns+5))
    print("\033[94m│ \033[95m1. SMS Bombing                                    \033[94m│".center(columns+5))
    print("\033[94m│ \033[95m2. Call Bombing                                   \033[94m│".center(columns+5))
    print("\033[94m└─────────────────────────────────────────────────────┘".center(columns+5))
    
    choice = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter your choice (1 or 2):> \033[37m")
    
    if choice == "1":
        sms_bombing_process()
    elif choice == "2":
        call_bombing_process()
    else:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mInvalid choice! Please select 1 or 2.\n")
        time.sleep(1)
        main_menu()

# SMS Bombing Process
def sms_bombing_process():
    global number, amount
    number = getNumber()
    amount = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount of SMS to Send:> \033[37m"))
    banner()
    
    # Call the SMS bombing function
    sms_bomb(number, amount)

# Call Bombing Process
def call_bombing_process():
    global number, amount
    number = getNumber()
    amount = int(input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount of Calls to Make:> \033[37m"))
    banner()
    
    for i in range(amount):
        call_bomb(number)
        time.sleep(5)  # Delay between calls

# Main Entry Point
if __name__ == "__main__":
    checkPy()
    update()
    main_menu()
