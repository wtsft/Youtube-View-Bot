import webbrowser
import time 
import os
import colorama

colorama.init()

print(  f"{colorama.Fore.RED}Made By JoseYt#1579")
print("Discord Server:https://discord.gg/3cDEYMdN")
print("""
╦┌─┐┌─┐┌─┐┌─┐  ╦ ╦╔╦╗  ╦  ╦┬┌─┐┬ ┬  ╔╗ ┌─┐┌┬┐
║│ │└─┐├┤ └─┐  ╚╦╝ ║   ╚╗╔╝│├┤ │││  ╠╩╗│ │ │ 
╝└─┘└─┘└─┘└─┘   ╩  ╩    ╚╝ ┴└─┘└┴┘  ╚═╝└─┘ ┴""" )
url = input("Enter the youtube URL:")
refresh = input("Enter the refresh time in seconds:")
count = input("How many views do you want? ")
 
def openURL():
    webbrowser.open(url)
    time.sleep(int(refresh))

    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()
 
openURL()