#!/usr/bin/env python3

import os

while True:
	os.system("pkg install toilet")
	os.system("clear")
	os.system("toilet -f mono12 -F gay TH27")
	print("""

[1] SocialMediaHackingTool
[2] Phishing

[0] Exit
               [h]Hakkında
""")

	islemno = input("TermuxHacker27: ")

	if islemno=="1":
		os.system("python config.py")
	elif islemno=='2':
		os.system("python config2.py")
	elif islemno=='0':
		quit()
	elif islemno=='h' or 'H':
		os.system("clear")
		os.system("toilet -f mono12 -F gay Bilgi")
		print("""
github Hesabım github.com/ekrem219

Daha Fazla Hack Için Telegram

Telegram Hesabım : t.me/TermuxHackBilgileri
""")
		input("TermuxHacker27:Ana Menü İçin Enter Bas")
	else:
		input("Hatalı Komut:")
	
