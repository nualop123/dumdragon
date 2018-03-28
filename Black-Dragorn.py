import sys, os, time
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
os.system("clear")
os.system("figlet Black Dragorn")
print " ======= Author: Zero Hacker TH ======= "
print " ======== DedSec CyderTeam TH ========= "
print "https://m.facebook.com/groups/181290935835347 "
print " ========== Anachakhacker ============= "
print "https://m.facebook.com/profile.php?id=436988319820662&ref=content_filter"
print "____________________________________________"
print
print
print (" [1] brute froce attack        ")
print (" [2] ddos attack               ")
print (" [3] virus                     ")
print (" [4] fishing                   ")
print (" [5] nmap scan                 ")
print
print ("[00] exit ")
print

A = raw_input("BDTools =>")

if A == "1" or A == "01":
    os.system("python2 blackhydra")

elif A == "2" or A == "02":
    ip = raw_input("IP Addrass :")
    port = raw_input("Port :")
    packet = raw_input("Packet :")
    os.system("python2 pntddos %s %s %s" %(ip, port, packet))

elif A == "3" or A == "03":
    os.system("python2 vbug")

elif A == "4" or A == "04":
    os.system("python2 weeman.py")

elif A == "5" or A == "05":
    print
    os.system("figlet NMap Scan")
    host = raw_input("IP or Host :")
    os.system("nmap %s" %(host,))

elif A == "19132":
    print "All List Porn Wedsite"
    print
    print "pornhub(http://www.pornhub.com)"
    print "xhamster(http://www.xhamster.com)"
    print "xvideo(http://www.xvideo.com)"
    print "xnxx(http://www.xnxx.com)"

elif A == "0" or A == "00":
    sys.exit()

else:
    print "\n[!] ERROR : Wrong Input"
    time.sleep(1)
    restart_program()
