#imports
import os
import time
from os import system, name
#batch commands
clear = lambda: os.system('dir /s')
dnscls = lambda: os.system('ipconfigg/flushDNS')
clls = lambda: os.system('cls')
binclear = lambda: os.system('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false')
#Credits
author = " DarkSaso "
version = " Version:1.0.0"
title = str.title("GLCleaner by" + author + version)
#important
print("IMPORTANT: before using the program read the #important section on the README.md")
print("if you have already read that section you can click ENTER to continue")
input("Press ENTER to continue...")
clls()
#code
print("░█▀▀█ ░█─── ░█▀▀█")
print("░█─▄▄ ░█─── ░█───")
print("░█▄▄█ ░█▄▄█ ░█▄▄█")
print("IMPORTANT: before using the program read the #important section on the README.md")
print("GLCleaner by "+author + version + "\n")
print("choose the type of cleaning to do:")
print("1)Standard\n2)Medium\n3)deep cleansing(SOON)")
start = input("Type:")
if(start == "1"):
    try:
        print("Staring...")
        clear()
        dnscls()
        clls()
        print("Completed :D\n\nThe Program Will be closed in 5sec")
    except:
        clls()
        print("Error: contact @DarkSaso on telegram or github")
if(start == "2"):
    print("This type of cleaning will delete files in the bin so you have to accept by typing 'accept' ")
    acc = input(".")
    if(acc == "accept"):
        try:
            print("Process started!")
            binclear()
            clear()
            dnscls()
            clls()
            print("Completed :D\nSupport\nTelegram: @DarkSaso\n\nThe Program Will be closed in 5sec")
        except:
            clls()
            print("Error(glc:execution_error): contact @DarkSaso on telegram or github")
    else:
        clls()
        print("you have chosen not to continue with the cleaning if you want to clean your recycle bin, restart the program and type {accept}")
if(start > str(2)):
    clls()
    print("This selection is not present or it will come with an upcoming update\n :(")
time.sleep(5)
