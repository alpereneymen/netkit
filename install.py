#!/usr/bin/python
import time,base64,urllib2,os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print  "                        Welcome To Php Print Installation                     "
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
while 1:
    cmd = raw_input(bcolors.BOLD + bcolors.FAIL +"\nNetkit (Install) > " + bcolors.ENDC)
    if cmd == "install":
        path = os.getcwd()
        fx = open("/usr/bin/netkit","w")
        fx.write("#!/bin/bash\ncd " + path + "&&" + "python " + path + "/netkit.py")
        os.system("chmod +x /usr/bin/netkit")
        print bcolors.BOLD + "Installation finished succesfully" + bcolors.ENDC
    if cmd == "uninstall":
        os.system("rm /usr/bin/netkit")
        print bcolors.BOLD + "Uninstallation finished succesfully" + bcolors.ENDC
    if cmd == "clear":
        os.system("clear")
    if cmd == "exit":
        break
    if cmd == "help":
        print bcolors.BOLD + bcolors.OKBLUE + "Help Menu" +bcolors.ENDC
        print "help : For see a Help Menu"
        print "clear : For clear terminal"
        print "exit : For exit"
        print "install : For started to installation"
        print "uninstall : For started to uninstallation"
        print "repair : For started to repair tools"
