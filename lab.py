# https://github.com/alpkeskin


from colors import bcolors
def app():
	try:
		import pyautogui
		import time
	except:
		print(bcolors.WARNING + "Error! You have to download the required module. Write this to your terminal : pip install PyAutoGUI "+ bcolors.ENDC)
	print(bcolors.OKCYAN +"Click where you want to write." + bcolors.ENDC)
	try:
		time.sleep(5)
		f = open("commands.txt", "r")
		for word in f:
			pyautogui.typewrite(word)
			time.sleep(2)
			if (word == "Q" or word == "q"):
				print("Done.")
				pyautogui.press("enter")
				f.close()
				exit()
	except KeyboardInterrupt:
		print("Exit.")




choice = input(bcolors.OKCYAN + "Does your instructor use asciicinema to give DEMO? y/n\n"+ bcolors.ENDC)

if(choice == "y" or choice == "Y"):

	try:
		import pyautogui
		import time
	except:
		print("Error! You have to download the required module. Write this to your terminal : pip install PyAutoGUI ")


	try:
		import urllib.request
		import os
		
		print(bcolors.OKBLUE + "Asciicinema ID girin." + bcolors.ENDC)
		print( "Example: https://asciinema.org/a/"+ bcolors.OKGREEN+ "zMC8F4pewPiEZS8wJq0CyT5fG"+ bcolors.ENDC)
		print( "Example ID is: "+ bcolors.OKGREEN+ "zMC8F4pewPiEZS8wJq0CyT5fG"+ bcolors.ENDC)
		id = input("")
		url = 'https://asciinema.org/a/' + id +'.cast?dl=1'
		file_path = os.path.dirname(os.path.abspath(__file__))
		urllib.request.urlretrieve(url, file_path + "\\command.cast")
		print(bcolors.OKGREEN + 'Beginning file download' + bcolors.ENDC)
		print(bcolors.OKGREEN + 'File is saved as command.cast' + bcolors.ENDC)
	except:
		print("Error!")
	f = open("command.cast", "r")
	liste =[]
	for word in f:
		if (len(word) <36):
			if "\\u001b" in word:
				word = word[word.find("\\u001b") + 9:]
			liste.append(word[word.find('"o", "') +6: len(word) - 3])
			
	st = ""
	cmdList = []

	for item in liste:
		if("\\r\\n" not in item and "\\r" not in item and "\\n" not in item):
			st += item
		else:
			if(st != "" or st != " "):
				cmdList.append(st)
				st = ""
	import os
	file_path = os.path.dirname(os.path.abspath(__file__))
	os.remove(file_path +"\\commands.txt")
	file_object = open('commands.txt', 'a')

	for line in cmdList:
		if line != '' and line != ' ' and line != '\n':
		
			file_object.write(line)
			file_object.write("\n")
	file_object.close()
	print(bcolors.OKGREEN + bcolors.BOLD+ 'Commands are parsed and saved as commands.txt' + bcolors.ENDC)

	
	app()
else:
	app()
