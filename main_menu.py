
import os
import getpass
import menu_awscli as aws
import hadoop as hp
import linux as lx
import docker as dr


def login():
	os.system('clear')
	os.system("tput setaf 6")
	print("\n\n\t\t-------Login to your TUI application-------\n\n")
	os.system("tput setaf 7")
	app_Pass = getpass.getpass("Enter password to start application: ")
	return app_Pass

while True:

	x=login()
	if x =='redhat':

		while True:
			os.system("tput setaf 3")
			print("\t\t\t-----------------------------\n\t\t\tWelcome to TUI Automated menu \n\t\t\t-----------------------------")
								

			os.system("tput setaf 6")
			print("""
				\n
				Press 1 :  RHEL8 O.S. 
				Press 2 :  AWS 
				Press 3 :  Hadoop
				Press 4 :  Docker

				Press 0 :  Exit
				""" )
			os.system("tput setaf 7")
			main = input("Enter your choice: ")

			if int(main) == 1:
				lx.contol_menu()
			elif int(main) == 2:
				aws.aws_login()
			elif int(main)==3:
				hp.menu()
			elif int(main)==4:
				dr.local()
			elif int(main)==0:
				exit()
			else:
				print('Wrong Input')
				input('Press enter to continue')
			os.system('clear')
					
		

	else:
		ch=input('Wrong Password\nContinue?\'y\' or \'n\': ')
		if ch=='y':
			os.system('clear')
			continue
		else:
			exit()

	
	
	
