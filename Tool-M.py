import time
import os
import random
import compileall
os.system ("clear")
print ("\033[1;31m                      _                    _")
time.sleep(0.2)
print ("                  ,/                        \,")
time.sleep(0.2)
print ("\033[1;30m        _________{(                          })_________")
time.sleep(0.2)
print ("\033[1;31m       / ------- /\\                         //\ -------.")
time.sleep(0.2)
print ("\033[1;32m      //@@@@@@@//@@\\  )                  (  //@@\\@@@@@@@\\")
time.sleep(0.2)
print ("\033[1;33m     //@@@@@@@//@@@@>>/                   \<<@@@@\\@@@@@@@\\")
time.sleep(0.2)
print ("\033[1;34m    //O@O@O@O//@O@O//                      \\\O@O@\\O@O@O@O\\")
time.sleep(0.2)
print ("\033[1;35m  //OOOOOOOO//OOOO||\033[1;35m           \  /   	   \033[1;35m||OOOO\\OOOOOOOO\\")
time.sleep(0.2)
print ("\033[1;36m (//O%O%O%O%//O%O%O%\\\033[1;35m         ))((    	   \033[1;36m//%O%O%O\\%O%O%O%O\\")
time.sleep(0.2)                                                                                
print ("\033[1;37m (||%%%%%%%%//'  `%%%%\\\033[1;35m      //  \\      \033[1;37m //%%%%'   `\\%%%%%%%||")
time.sleep(0.2)                                                                                      
print ("\033[1;32m ((%%%%%%%((      %%%%%\\\033[1;35m    ((    ))   \033[1;32m //%%%%%       ))%%%%%%))")
time.sleep(0.2)
print ("\033[1;32m  \:::' `::\\      `:::::\\\33[1;35m    \)~~(/   \033[1;32m //:::::'      //::' `:::/")
time.sleep(0.2)
print ("\033[1;32m   )'     `;)'      (`  ` \\\033[1;35m `<@  @>'\033[1;32m / / '  ')      `(;'     `(")
time.sleep(0.2)
print ("\033[1;32m          (               \`\\ \033[1;35m)^^(\033[1;32m/  /               )     ")
time.sleep(0.2)
print ("\033[1;32m         _                  ) \\oo/   (                      ")
time.sleep(0.2)
print ("\033[1;31m       (@)                  \  `'   /                      _")
time.sleep(0.2)
print ("       \033[1;31m|-|\__________________\__^__<________oOo__________ (@)")
time.sleep(0.2)
print ("       \033[1;31m| |                                  VVV          \|-|")
time.sleep(0.2)
print ("       \033[1;31m|-|              \033[1;34mWELCOME TO TOOL-M                 \033[1;31m|-|")
time.sleep(0.2)
print ("\033[1;31m       |_|\_____________________________________________  | |")
time.sleep(0.2)
print ("\033[1;31m       (@)\033[1;33m                 / ,/ \_____/ \\ ~\/~          \033[1;31m`\|-|")
time.sleep(0.2)
print ("\033[1;33m        ~             ___//^~      \____/\\                \033[1;31m(@)")
time.sleep(0.2)
print ("\033[1;33m                     <<<  \     __  <____/||               ~")
time.sleep(0.2)
print ("\033[1;33m                               <   \ <___/||")
time.sleep(0.2)
print ("                                  || <___//")
time.sleep(0.2)
print ("                                  \ \/__//")
time.sleep(0.2)
print ("                                   ~----~")
time.sleep(0.2)
mixh = """
\033[1;34m^===========================================^
||					   ||
||  \033[1;31m[1]   ==> cipher Tools  	           ||
||  \033[1;32m[2]   =>> Guess Nummber		   ||
||  \033[1;33m[3]   =>> strong passwords list	   ||
||  \033[1;34m[4]   =>> info Tool			   ||
||  \033[1;35m[ex]  =>> exit tool			   ||
||  \033[1;36m[cls] =>> clear screan		   ||
||  \033[1;31m[up]  =>> update Tool		   ||
\033[1;34m^===========================================^
"""
print (mixh)
#######++++++++++++#######+++++++++$$$$###$$##
print ("👉-----[ Tool-M 💀 ]----👈")
print ("|")
mck = input ("\033[1;36mchoose Nummber \033[1;31m=\033[1;32m=> ")
#_______________________________xxx _defs xxx__________________
def info  (ter) :
	print ("Tool Name => Tool-M ")
	print ("vairson => v2 ")
	print ("language => python ")
	print ("By => Michael Meled 'Team MD'")
	print ("work => kali linux - termux - nh ")
def clear (clear) :
	os.system ("clear")
	os.system ("python3 Tool-M.py")
def exit (exit) :
	print ("thank you use Tool-M")
	os.system ("exit") 
#____________________________help______________________
def help (help) :
	print  ("help codec ")
	vy = """
	1- New Folder 
	2- choose Tool codec
	3- write 'mv (Name Tool) Tool-M_file_code'
	4- run Tool-M.py
	5- choose Nummber (1)
	6- => succid cipher Tool <=
	"""
	print (vy)
	os.system ("mkdir Tool-M_file_code")
	mic = input ("choose Name file ==> ")
	compileall.compile_dir(mic)
#________________________xxx _defs xxx_________________________
def password (banner) :
	pw = ["23hbmnrd#","$6755fdncd79$$99","dsnbfd$","1234xgdhfhde$%&#","qwertyuiop1023097398474983@$#&$$a","12345678qweasdzx&%$$#xcv"]
	for i in range (50000) :
		print ("\033[1;34m{",i,"}","\033[1;31m×>>\033[1;32m",random.choice(pw))

def GetPassword(data):
        Max = 13
        password ="+2012"
        while len(password) != Max:
                value = random.choice(data)
                password += value
        return password

def banner (ban) :
        data = '1234567890'
        mi = ":1122334455"
        for i in range(50000):
                print ("\033[1;36m[",i,"]","\033[1;32m==>\033[1;31m",GetPassword(data),":1122334455")

## if ###
if mck == "1" :
	help ("123")

if mck == "2" :
	banner ("123")

if mck == "3" :
	password ("123")

if mck == "4" :
	info ("123")

if mck == "cls" :
	os.system ("clear")
	os.system ("python3 Tool-M.py")

if mck == "ex" :
	os.system ("exit")
