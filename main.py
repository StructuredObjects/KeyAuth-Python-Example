from keyauth import api
import os
import sys
import os.path
import platform
from time import sleep
from datetime import datetime

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA
os.system("cls")
os.system("title Python Example")
print("Initializing")
keyauthapp = api(
	name = "",
	ownerid = "",
	secret = "",
	version = "1.0",
)
print ("""
1.Login
2.Register
3.Upgrade
4.License Key Only
""")
print(f"""
App data:
Number of users: {keyauthapp.app_data.numUsers}
Number of online users: {keyauthapp.app_data.onlineUsers}
Number of keys: {keyauthapp.app_data.numKeys}
Application Version: {keyauthapp.app_data.app_ver}
Customer panel link: {keyauthapp.app_data.customer_panel}
""")
sleep(1.5) # rate limit
print(f"Current Session Validation Status: {keyauthapp.check()}")
sleep(1.5) # rate limit
print(f"Blacklisted? : {keyauthapp.checkblacklist()}") # check if blacklisted, you can edit this and make it exit the program if blacklisted

ans=input("Select Option: ") 
if ans=="1": 
	user = input('Provide username: ')
	password = input('Provide password: ')
	keyauthapp.login(user,password)
elif ans=="2":
	user = input('Provide username: ')
	password = input('Provide password: ')
	license = input('Provide License: ')
	keyauthapp.register(user,password,license) 
elif ans=="3":
	user = input('Provide username: ')
	license = input('Provide License: ')
	keyauthapp.upgrade(user,license)
elif ans=="4":
	key = input('Enter your license: ')
	keyauthapp.license(key)
elif ans !="":
	print("\nNot Valid Option") 
	sys.exit()

print("\nUser data: ") 
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
print("Subcription: " + keyauthapp.user_data.subscription)
print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Current Session Validation Status: {keyauthapp.check()}")
print("Exiting in 10 secs....")
sleep(10)
exit(0)
