import os

def local():
	def dr_repo():
		name=input('Enter repo name: ')
		os.system('cd /etc/yum.repos.d/')
		os.system('touch {}.repo'.format(name))
		with open('/etc/yum.repos.d/{}.repo'.format(name),'w+') as r:
			r.write('[{}]'.format(name))
			r.write('\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/')
			r.write('\ngpgcheck=0')
		print('Docker repo created successfully')
		os.system('cat /etc/yum.repos.d/{}.repo'.format(name))
		input("\n\nPress enter to continue")



	def dr_install():
		print("Checking if docker installed or not")
		os.system('rpm -q docker-ce')
		ch=input('Continue to install ? \'y\' or \'n\': ')
		if ch=='y':
			os.system('yum install docker-ce --nobest -y')
			os.system('firewall-cmd --zone=public --add-masquerade --permanent')
			os.system('firewall-cmd --zone=public --add-port=80/tcp --permanent')
			os.system('firewall-cmd --zone=public --add-port=443/tcp --permanent')
			os.system('firewall-cmd --reload')
			os.system('setenforce 0')
			input("\nPress enter to continue")
		else:
			return

	
	def dr_daemon():
		print("""Docker daemons :-
			1.To start
			2.To enable (permanent)
			3.To stop
			4.For status
			""")
		ch=input("Enter your choice: ")
		if ch=='1':
			os.system('systemctl start docker')
			os.system('systemctl status docker')
		elif ch=='2':
			os.system('systemctl enable docker')
			os.system('systemctl status docker')
		elif ch=='3':
			os.system('systemctl stop docker')
			os.system('systemctl status docker')
		elif ch=='4':
			os.system('systemctl status docker')
		input("\nPress enter to continue")


	def dr_pullImg():
		name=input("Enter os name: ")
		print('Searching for image......\n\n')
		os.system('docker search {}'.format(name))
		ch=input('Continue to pull image ? \'y\' or \'n\': ')
		if ch=='y':
			version=input("Enter os version: ")
			os.system('docker pull {}:{}'.format(name,version))
			input("\nPress enter to continue")
		else:
			return

	def dr_delImg():
		print('\n\t\tList of avilable images:-\n')
		os.system ('docker images')
		name=input("Enter image name: ")
		version=input("Enter os version: ")
		os.system('docker rmi {}:{}'.format(name,version)) 
		input("\nPress enter to continue")

	def dr_delCon():
		print('\n\t\tList of all container:-\n')
		os.system ('docker ps -a')
		name=input("Enter container name: ")
		os.system('docker rm {}'.format(name))


	def dr_launch():
		name=input("Enter container name: ")
		print('\n\t\tList of avilable images:-\n')
		os.system ('docker images')
		img_name=input("\n\nEnter image name: ")
		version=input("Enter version: ")
		os.system('setenforce 0')
		os.system('docker run -it --name {} {}:{}'.format(name,img_name,version))

	def dr_startCon():
		print('\n\t\tList of all container:-\n')
		os.system ('docker ps -a')
		name=input("Enter container name: ")
		os.system("docker start {}".format(name))
		input("\nPress enter to continue")

	def dr_stopCon():
		print('\n\t\tList of running container:-\n')
		os.system ('docker ps ')
		name=input("Enter container name: ")
		os.system("docker stop {}".format(name))
		input("\nPress enter to continue")

	def dr_run1cmd():
		print('\n\t\tList of avilable images:-\n')
		os.system ('docker images')
		name=input("\n\nEnter image name: ")
		version=input("Enter version: ")
		cmd=input("Enter your command: ")
		os.system("docker run -i {}:{}  {}".format(name,version,cmd))
		input("\nPress enter to continue")				
		
	def dr_runCon():
		print('\n\t\tList of running container:-\n')
		os.system ('docker ps')
		name=input("Enter container name: ")
		os.system("docker attach {}".format(name))
		input("\nPress enter to continue")

	def dr_logs():
		print('\n\t\tList of all containers:-\n')
		os.system ('docker ps -a')
		name=input("Enter container name: ")
		os.system("docker logs {}".format(name))
		input("\nPress enter to continue")
		


	def dr_copy():
		print("""\n\t\tHelp:-
			1.container path= <container name>:<path> (e.g. web1:/root/)
			2.baseOS path= e.g. /sweety.txt
			""")
		src=input("Enter source file path: ")
		dest=input("Enter destination directory path: ")
		os.system('docker cp {} {}'.format(src,dest))
		input("\nPress enter to continue")

		



	while True:
		os.system("tput setaf 3")
		print("\t\t\t--------------------------\n\t\t\t   Welcome to Docker menu\n\t\t\t--------------------------")
                                  
                               
		os.system("tput setaf 6")
		print("""\n\n\t\t
			1.To configure docker repo
			2:To install docker
			3:To see docker information
			4:To start/stop/enable/see status of docker
			5:To pull image
			6:To see available images
			7:To delete image
			8:To check running container
			9:To see all container
			10:To delete container 
			11:To launch container
			12:To start container
			13:To stop container
			14:To run container for particular/single command
			15:To run container with terminal
			16:To see logs
			17:To transfer file to/from container and baseOS

			0:To Exit
                	""")
		os.system("tput setaf 7")
		dr=input("Enter your choice: ")
		if int(dr)==1:
			dr_repo()
		elif int(dr)==2:
			dr_install()
		elif int(dr)==3:
			os.system('docker info')
			input("\nPress enter to continue")
		elif int(dr)==4:
			dr_daemon()
		elif int(dr)==5:
			dr_pullImg()
		elif int(dr)==6:
			os.system('docker images')
			input("\nPress enter to continue")
		elif int(dr)==7:
			dr_delImg()
		elif int(dr)==8:
			os.system('docker ps')
			input("\nPress enter to continue")
		elif int(dr)==9:
			os.system('docker ps -a')
			input("\nPress enter to continue")
		elif int(dr)==10:
			dr_delCon()
		elif int(dr)==11:
			dr_launch()	
		elif int(dr)==12:
			dr_startCon()
		elif int(dr)==13:
			dr_stopCon()
		elif int(dr)==14:
			dr_run1cmd()
		elif int(dr)==15:
			dr_runCon()
		elif int(dr)==16:
			dr_logs()
		elif int(dr)==17:
			dr_copy()

		elif int(dr)==0:
			break;
		else:
			print("Wrong Input")
			input("\nPress enter to give input again")

						
		os.system('clear')





	
