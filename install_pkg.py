import os
os.system ("clear")
def banner (ban) :
	os.system ("clear")
	os.system ("pkg update && pkg upgrade")
	os.system ("pkg install python3")
	os.system ("rm -rif install_pkg.py")
print ("\033[1;32mrun Tool-M read pasword")
mick = input ("\033[1;31mwrite password ==> ")
if mick == "1234_Tool-M" :
	banner ("1133")
else:
	os.system ("python3 Tool-M.py")
