from datetime import datetime
import time
import urllib.request
print("Juli's lib imported all packages!")
def help():
	print("\n\n\njulislib.help()\n	Print this\n\njulislib.waituntil(hour,minute)\n\n 	Wait for hour:minute and continue executing")
def waituntil(hour, minute):
	hour=int(hour)
	minute=int(minute)
	while True:
		now = datetime.now()
		hours = hour - int(now.strftime("%H"))
		minutes = int(now.strftime("%M"))
		min_left = int(minute - minutes)
		currenttime = int(time.strftime("%M"))
		if min_left == 0 or min_left < 0:
			if hours == 0 or hours < 0:
				return
		while minutes == currenttime:
			currenttime = int(time.strftime("%M"))
			time.sleep(1)
def download(url,name):
	urllib.request.urlretrieve(url,name)
	return

print("Juli's lib finished load!"+'\n\nIf you want to have a play with my lib\nType "import julislib"\n\n"julislib.help()"\n\nFor help text')
