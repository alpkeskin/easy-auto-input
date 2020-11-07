# https://github.com/alpkeskin
try:
	import pyautogui
	import time
except:
	print("Error! You have to download the required module. Write this to your terminal : pip install PyAutoGUI ")
print("Click where you want to write.")
try:
	time.sleep(5)
	f = open("commands.txt", "r")
	for word in f:
		pyautogui.typewrite(word)
		time.sleep(2)
		if (word == "Q" or word "q"):
			print("Done.")
			pyautogui.press("enter")
			f.close()
			exit()
except KeyboardInterrupt:
	print("Exit.")
