'''
print ("MEDOS Beta build 2")
print ("Developer debug build")
print ("Checking Memory")
print ("Total disk space: 16 TB")
print ("Speed: 6 MB/S")
print ("32 bit processor")
print ("Current directory is FC:/")
print ("File count: 5")
print ("Memory used: 20000 bytes")
print ("Run a command to begin, type help for help")
in1 = input("FC:/")
if (in1 = ("dir")): 
	print ("Directory of FC1")
	print ("Test.txt")
	print ("Test.bmp")
	print ("Test.wav")
	print ("Test.py")
	print ("Test.rtf")
if (in1 = ("help")):
	print ("Help list")
	print ("DIR = Directory")
	print ("CLS = Clear screen")
	print ("HELP = Help guide")
	print ("RUN = Run a program/file")
	print ("DEL = Delete the selected file")
	print ("COLOR = Change the text color of the terminal")
	print ("EXIT = Shut down the system")
	print ("CD = Choose a directory, type .. or the directory name afterwards, and you will go to the next directory")
	print ("PLAY = Play the currently selected audio or video")
	print ("EJECT = Eject the system, make it ready for ejecting the drive")
	print ("NETW = Change the current network")
	print ("DISCON = Disconnect from the internet, go offline")
if (in1 = ("cls")):
	print ("This command is unavailable")
if (in1 = ("run")):
	print ("The syntax of the command is incorrect")
if (in1 = ("del")):
	print ("The syntax of the command is incorrect")
if (in1 = ("color")):
	print ("This command is unavailable")
if (in1 = ("exit")):
	print ("This command is unavailable")
if (in1 = ("CD")):
	print ("This command is unavailable")
if (in1 = ("play")):
	print ("This command is unavailable")
if (in1 = ("eject")):
	print ("The syntax of the command is incorrect")
if (in1 = ("netw")):
	print ("This command is unavailable")
if (in1 = ("discon")):
	print ("This command is unavailable")
else:
	print (in1)
'''
print ("MEDOS Beta build 1")
print ("Developer debug build")
print ("Checking Memory")
print ("Total disk space: 16 TB")
print ("Speed: 6 MB/S")
print ("32 bit processor")
print ("Current directory is FC:/")
print ("File count: 5")
print ("Memory used: 20000 bytes")
print ("Run a command to begin, type help for help")
in1 = input("FC:/")
if (in1 == ("dir")): 
    print ("Directory of FC1")
    print ("Test.txt")
    print ("Test.bmp")
    print ("Test.wav")
    print ("Test.py")
    print ("Test.rtf")
	else:
		if (in1 == ("help")):
			print ("Help list")
			print ("DIR = Directory")
			print ("CLS = Clear screen")
			print ("HELP = Help guide")
			print ("RUN = Run a program/file")
			print ("DEL = Delete the selected file")
			print ("COLOR = Change the text color of the terminal")
			print ("EXIT = Shut down the system")
			print ("CD = Choose a directory, type .. or the directory name afterwards, and you will go to the next directory")
			print ("PLAY = Play the currently selected audio or video")
			print ("EJECT = Eject the system, make it ready for ejecting the drive")
			print ("NETW = Change the current network")
			print ("DISCON = Disconnect from the Internet, go offline")
			else:
				if (in1 == ("cls")):
					print ("This command is unavailable")
					else:
						if (in1 == ("run")):
							print ("The syntax of the command is incorrect")
							else:
								if (in1 == ("del")):
									print ("The syntax of the command is incorrect")
									else:
										if (in1 == ("color")):
											print ("This command is unavailable")
											else:
												if (in1 == ("exit")):
													print ("This command is unavailable")
													else:
														if (in1 == ("CD")):
															print ("This command is unavailable")
															else:
																if (in1 == ("play")):
																	print ("This command is unavailable")
																	else:
																		if (in1 == ("eject")):
																			print ("The syntax of the command is incorrect")
																			else:	
																				if (in1 == ("netw")):
																					print ("This command is unavailable")
																					else:
																						if (in1 == ("discon")):
																							print ("This command is unavailable"
																							else:
																								print (in1)