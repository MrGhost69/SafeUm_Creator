import requests, random, requests, json, pyfiglet,sys,time, os, uuid, webbrowser, fake_useragent

Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("SafeUm")
print(a_bSa+ab)


E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

line = "(+)==============================================(+)"
logo=(f""" \033[1;37m 
  7MMMMMMq.   .MMMMbYd 7MMM.     ,MMF'
    MM   MM. ,MI    "Y   MMMb    dPMM  
    MM   ,M9  MMb.       MM M   ,M MM  
    MMmmdM9     YMMNq.   MM  M  M' MM  
    MM  YM.   .     MM   MM  'MP'  MM  
    MM   `Mb. Mb     dM   MM   M    MM  
  .TMML. .JMM PKYbmmd"  .JMML.    .JMML. 
{line}
  Owner       :- Mr.Ghost
  Version     :- 0.1
  tool       :- SAFE UP AUTO CREATE 
{line}""")
print('')

print('\033[32;m')

from os import system,name
from ssl import CERT_NONE
from gzip import decompress
from random import choice,choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
try:
 from websocket import create_connection
except:
 system('pip install websocket-client')
 from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []
print(f'{line}')       
def work():
 global failed,success,retry
 username = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
 try:
  con = create_connection("wss://193.200.173.45/Auth", header={"app": "com.safeum.android","host": None,"remoteIp": "193.200.173.45","remotePort": str(8080),"sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195","time": "2023-04-30 12:13:32","url": "wss://51.79.208.190/Auth"},sslopt={"cert_reqs": CERT_NONE})
  con.send(dumps({"action":"Register","subaction":"Desktop","locale":"en_GB","gmt":"+02","password":{"m1x":"503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc","m1y":"6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc","m2":"219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf","iv":"e38cb9e83aef6ceb60a7a71493317903","message":"0d99759f972c527722a18a74b3e0b3c6060fe1be3ad53581a7692ff67b7bb651a18cde40552972d6d0b1482e119abde6203f5ab4985940da19bb998bb73f523806ed67cc6c9dbd310fd59fedee420f32"},"magicword":{"m1x":"04eb364e4ef79f31f3e95df2a956e9c72ddc7b8ed4bf965f4cea42739dbe8a4a","m1y":"ef1608faa151cb7989b0ba7f57b39822d7b282511a77c4d7a33afe8165bdc1ab","m2":"4b4d1468bfaf01a82c574ea71c44052d3ecb7c2866a2ced102d0a1a55901c94b","iv":"b31d0165dde6b3d204263d6ea4b96789","message":"8c6ec7ce0b9108d882bb076be6e49fe2"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi Redmi Note 8 Pro","softwareversion":"1.1.0.1380","nickname":"hvtctchnjvfxfx","os":"AND","deviceuid":"c72d110c1ae40d50","devicepushuid":"*dxT6B6Solm0:APA91bHqL8wxzlyKHckKxMDz66HmUqmxCPAVKBDrs8KcxCAjwdpxIPTCfRmeEw8Jks_q13vOSFsOVjCVhb-CkkKmTUsaiS7YOYHQS_pbH1g6P4N-jlnRzySQwGvqMP1gxRVksHiOXKKP","osversion":"and_11.0.0","id":"1734805700"}))
  gzip = decompress(con.recv()).decode('utf-8')
  if '"status":"Success"' in gzip:
   success+= 1
   b = accounts.append(username+':hhhh')
   print(b)
   with open('SafeUM-Accounts-bd.txt', 'a') as f: f.write(username + ":hhhh\n")
   
  else:
   failed+=1
 except: retry+=1

start = ThreadPoolExecutor(max_workers=1000)
    
while True:
    
    start.submit(work)
    print(''+ ' ' * 25 + 'Success : ' + str(success) + '' + ' ' * 25 + 'Failed : ' + str(failed) + '' + ' ' * 25 + 'ReTry : ' + str(retry))
   # sys.stdout.write(f'\r\r{A}({A}START- M3{A}){A} %s {A}|{A} OK{A}|{PPP}CP{A} %s{A}|{A}%s | try %s'%(str(success),str(failed),str(retry)));sys.stdout.flush()
    hh = str(failed) + str(success) + str(retry)
    if int(retry) > int(1500):
        print('')
    if int(success) > int(0):
        z = "\n".join(accounts)
        print("CREATED ACCOUNTS>>\n",z)
    os.system('clear') 
