import os
import getpass


def control_menu():
	os.system("tput setaf 3")
	print("\t\t\tWelcome to Redhat TUI")	
	os.system("tput setaf 7")
	print("..................................................................")

	'''app_Pass = getpass.getpass("enter password to start application")
	opass = "redhat" 
	if app_Pass != opass:
		print("please enter correct password ")
	else : '''
	location =input("where you want to run command(remote/local)")
	print(location)

	if location =="remote":
		linux_Menu_Remote()
	if location == "local":
		linux_Menu_Local()
	else:
		print("invalid input")


                                        
def create_User_Local():
	user_Name= input("enter user name")	
	os.system("useradd {0}".format(user_Name))
	print("User created Successfully")

def create_User_Remote():
	user_Name= input("enter user name")	
	os.system("sshpass -p {0} ssh {1} useradd {2}".format(remote_Ip,file_name,user_Name))
	print("User created Successfully")



def create_File_Local():
	file_name=input("enter filename")
	os.system("vi {0}".format(file_name))
	print("{0} file created".format(file_name))

def create_File_Remote():
	file_name=input("enter filename")
	os.system("ssh {0} vi {1}".format(remote_Ip,file_name))
	print("{0} file created".format(file_name))




def launch_Httpd_Server_Local():
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("systemctl status httpd")


def launch_Httpd_Server_Remote():
	os.system("sshpass -p {0} ssh {1} yum install httpd -y".format(remote_Pass,remote_Ip))
	os.system("sshpass -p {0} ssh {1} systemctl start httpd".format(remote_Pass,remote_Ip))
	os.system("sshpass -p {0} ssh {1} systemctl status httpd".format(remote_Pass,remote_Ip))





def create_Lv ():
	pv = input("Enter Your Device Name To Create Physical Volume (ex- sdb): ")
	os.system('pvcreate /dev/{}'.format(pv))
	print('PV Created..!')
	os.system('pvdisplay /dev/{}'.format(pv))
	vg = input("Enter Volume Group Name: ")
	pv = input("Enter Physical Volume Name (ex- sdb): ")
	os.system('vgcreate {} /dev/{}'.format(vg, pv))
	print('VG Created..!')
	os.system('vgdisplay {}'.format(vg))
	lv = input('Enter Logical Volume Name: ')
	sz = input('Enter LV Size: ')
	os.system('lvcreate --size {} --name {} {}'.format(sz, lv, vg))
	print('LV Created..!')
	os.system("lvdisplay {}/{}".format(vg, lv))
	print('Formatting Your LV...')
	os.system('mkfs.ext4 /dev/{}/{}'.format(vg, lv))
	print("LV Formatted..!")





def mount_Lv():
	create_directory()
	lv = input("Enter Logical Volume Name : ")
	vg = input("Enter Volume Group Name : ")
	path = input("Enter Your LV Mount Point Name : ")              	
	os.system("mount /dev/{}/{}  /{}".format(vg, lv, path))
	print("LV Mounted..!")
	os.system('df -hT')



def create_directory():
	dir=input("Enter folder name ")
	os.system('mkdir /{0}'.format(dir))
	print('{0} directory created '.format(dir))




def extend_Lvm ():
	lv = input("Which LV You Want To Extend?: ")
	vg = input("Enter LV Group Name: ")
	sz = input("How Much Size You Want To Extend?: ")                  	
	os.system('lvextend --size +{} /dev/{}/{}'.format(sz, vg, lv))
	print("Re-Formatting LV...")
	os.system('resize2fs  /dev/{}/{}'.format(vg, lv))
	print("Extended LV Size..!")
	os.system('df -hT')


def reduce_Lvm ():
	lv = input("Which LV You Want To Reduce?: ")
	vg = input("Enter LV Group Name: ")
	sz = input("How Much Size You Want To Reduce?: ")
	os.system('lvreduce --size -{} /dev/{}/{}'.format(sz, vg, lv))
	print("Sucessfully reduced the Size of LVM Partition..!")
	print("Re-Formatting LV...")
	os.system('resize2fs  /dev/{}/{}'.format(vg, lv))
	print("Reduced LV Size..!")      
	os.system('lvdisplay {0}/{1}'.format(vg,lv))






def linux_Menu_Local():
	while True:
		print("""linux
			press 1  : Date
			press 2  : calendar
			press 3  : IP Address
			press 4  : Task Runing in Backgroud 
			press 5  : Run background Task
			press 6  : Create file 
			press 7  : List of All Hardisk 	
			press 8  : Launch Firefox
			press 9  : Create User
			press 10 : Launch HTTP server
			press 11 : Create Logical Volume 	
			press 12 : Mount Logical Volume 
			press 13 : Increase or Decrease Logical Volume size

			""")
		linux  = input ("select Linux command to Run   " )
		if int(linux) == 1:
			os.system("date")
		elif int(linux) == 2:
			os.system("cal")
		elif int(linux) == 3:
			os.system("ifconfig")
		elif int(linux) == 4:
			os.system("jobs")
		elif int(linux) == 5:
			os.system("fg")
		elif int(linux) == 6:
			create_File_Local()
		elif int(linux) == 7:
			os.system("fdisk -l")
		elif int(linux) == 8:
			os.system("firefox")
		elif int(linux) == 9:
			create_User_Local()
		elif int(linux) == 10:
			launch_Httpd_Server_Local()
		elif int(linux) == 11:
			create_Lv ()
		elif int(linux) == 12:
			mount_Lv ()
		elif int(linux) == 13:
			x = input("Do You Want To Extend or Reduce The Size of LV?: ")
			if x == "extend":
				extend_Lvm ()
			elif x == "reduce":
				reduce_Lvm ()
		input("please enter to continue")
		os.system("clear")		




def linux_Menu_Remote():
	remote_Ip = input("Enter remote IP Address")
	remote_Pass = input("Enter password")
	while True:
		print("""linux
				press 1  : Date
				press 2  : calendar
				press 3  : IP Address
				press 4  : Task Runing in Backgroud 
				press 5  : Run background Task
				press 6  : Create file
				press 7  : List of All Hardisk 	
				press 8  : Launch Firefox
				press 9  : Create User
				press 10 : Launch HTTP server
				
				""")

		linux  = input ("select Linux command due you want to Run" )
		if int(linux) == 1:
			os.system("sshpass -p {0} ssh {1}date".format(remote_Pass,remote_Ip))
		elif int(linux) == 2:
			os.system("sshpass -p {0} ssh {1} cal ".format(remote_Pass,remote_Ip))
		elif int(linux) == 3:
			os.system("sshpass -p {0} ssh {1} ifconfig ".format(remote_Pass,remote_Ip))
		elif int(linux) == 4:
			os.system("sshpass -p {0} ssh {1} jobs ".format(remote_Pass,remote_Ip))
		elif int(linux) == 5:
			os.system("sshpass -p {0} ssh {1} fg ".format(remote_Pass,remote_Ip))
		elif int(linux) == 6:
			create_File_Remote()			
		elif int(linux) == 7:
			os.system("sshpass -p {0} ssh {1} fdisk -l".format(remote_Pass,remote_Ip))
		elif int(linux) == 8:
			os.system("sshpass -p {0} ssh {1} firefox ".format(remote_Pass,remote_Ip))
		elif int(linux) == 9:
			create_User_Remote()			
		elif int(linux) == 10:
			launch_Httpd_Server_Remote()	

		input("please enter to continue")
		os.system("clear")		

