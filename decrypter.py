import ftplib
import argparse
from termcolor import colored
print(" ______ ______  _                 ")
print("|  ____|___  / | |                ")
print("| |__     / /  | |     ___   __ _ ")
print("|  __|   / /   | |    / _ \ / _` |")
print("| |     / /__  | |___| (_) | (_| |")
print("|_|    /_____| |______\___/ \__  |")
print(" _____                _      __/ |")    
print("|  __ \              | |    |___/ ")     
print("| |__) |___  __ _  __| | ___ _ __ ")
print("|  _  // _ \/ _` |/ _` |/ _ \ '__|")
print("| | \ \  __/ (_| | (_| |  __/ |   ")
print("|_|  \_\___|\__,_|\__,_|\___|_|   ")
print("")
print("----------------------------------")
parser = argparse.ArgumentParser()
parser.add_argument('-f','--file', help='Path to XML-file', required=True)
parser.add_argument('-v','--verify', action='store_true')
args = parser.parse_args()
print("Read from file: ",end="")
print(args.file)
print("----------------------------------")
print("----------------------------------")
fobj = open(args.file)
hosts=[]
users=[]
passs=[]
data=[]
for line in fobj:
    if not line.find("<Host>")==-1:
        hosts.append(line[18:line.find("</Host>")])
    elif not line.find("<User>")==-1:
        users.append(line[18:line.find("</User>")])
    elif not line.find("<Pass>")==-1:
        passs.append(line[18:line.find("</Pass>")])
fobj.close()
if args.verify:
    if len(hosts)==len(users) and len(users)==len(passs):
        rhosts=0
        rlogins=0
        for i in range(len(hosts)):
            richtigerHost=True
            try:
                ftp = ftplib.FTP(hosts[i])
                #ftp.set_debuglevel(2)
            except:
                #print("FALSCHER HOST!")
                richtigerHost=False
            richtigerLogin=True
            try:
                ftp.login(users[i],passs[i])
            except:
                #print("FALSCHER LOGIN!")
                richtigerLogin=False
            data.append([hosts[i],users[i],passs[i],richtigerHost,richtigerLogin])
            if richtigerHost:
                print(colored('HOST: ',"green"),end="")
                print(colored(hosts[i],"green"))
                rhosts+=1
            else:
                print(colored('HOST: ',"red"),end="")
                print(colored(hosts[i],"red"))

            if richtigerLogin:
                print(colored('USER: ',"green"),end="")
                print(colored(users[i],"green"))
                print(colored('PASS: ',"green"),end="")
                print(colored(passs[i],"green"))
                rlogins+=1
            else:
                print(colored('USER: ',"red"),end="")
                print(colored(users[i],"red"))
                print(colored('PASS: ',"red"),end="")
                print(colored(passs[i],"red"))
            print("---------------------------------------")
        
    else:
        print("Datei ist nicht symmetrisch!")
    print("---------------------------------------")
    print("---------------------------------------")
    print("RESULT:   ",rhosts," SERVER(S) UP   ",rlogins," LOGINS CORRECT")
else:
    if len(hosts)==len(users) and len(users)==len(passs):
        for i in range(len(hosts)):
            data.append([hosts[i],users[i],passs[i]])
            print(colored('HOST: ',"green"),end="")
            print(colored(hosts[i],"green"))
            print(colored('USER: ',"green"),end="")
            print(colored(users[i],"green"))
            print(colored('PASS: ',"green"),end="")
            print(colored(passs[i],"green"))
            print("---------------------------------------")
        
    else:
        print("Datei ist nicht symmetrisch!")
    print("---------------------------------------")
    print("---------------------------------------")
    print("RESULT:  USE ARGUMENT -v / --verify TO CHECK PASSWORDS")
