import os
import getpass

def aws_login():
	os.system('tput setaf 6')
	print("\t\t-------Login to your aws account-------\n\n")
	os.system('tput setaf 7')
	os.system("aws configure")
	awsMenu()


def awsMenu():

	
	def launch_inst():
		
		print("""\n\nSelect image-type:-
		                0. Amazon Linux 2
				1. RHEL 8 
				 """)
		image_l=['ami-0e306788ff2473ccb','ami-0e306788ff2473ccb']
		image=image_l[int(input('Enter your choice: '))]


		print("""\n\nSelect instance-type
				0.t2.micro
				1.t2.small
				2.t2.medium
				""")
		i_type=['t2.micro','t2.small','t2.medium']
		inst_type=i_type[int(input('Enter your choice: '))]

		print("\n\nEnter no. of instances to launch: ")
		count=int(input())

		os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {}'.format(image,inst_type,count))
		input("\nPress enter to continue")

	def create_key_pair():
		name=input("Enter key-name: ")
		os.system('aws ec2 create-key-pair --key-name {}'.format(name))
		input("\nPress enter to continue")

	def create_S3_bucket():
		name=input("Enter bucket name: ")
		print("""Select region:-
			0.North virginia
			1.Mumbai
			""")
		code=['us-east-1','ap-south-1']
		region=code[int(input('Enter your choice: '))]

		os.system('aws s3api create-bucket --bucket {}  --region {} --create-bucket-configuration LocationConstraint={}'.format(name,region,region)) 
		input("\nPress enter to continue")

	def transfer_S3():
		print("""\n\t\tHelp:-
		1.local= /root/menu.png  (example)
		2.S3uri= s3://<bucketname>/<folder/file path>
		""")
		source=input("Enter path of source file(local/S3uri): ")
		dest=input("Enter path of destination folder(local/S3uri): ")
		os.system('aws s3 cp {} {}'.format(source,dest))
		input("\nPress enter to continue")

	def create_EBS():
		print("""\n\t\tSelect availability-zone:-
			For North virginia region:-
			0.AZ-a
			1.AZ-b
			For Mumbai region:-
			2.AZ-a
			3.AZ-b
			""")
		az_code=['us-east-1a','us-east-1b','ap-south-1a','ap-south-1b']
		az=az_code[int(input("Enter your choice: "))]
		print(az)
		size=input("Enter size of volume: ") 
		os.system('aws ec2 create-volume --availability-zone {} --no-encrypted --size {}'.format(az,size))
		input("\nPress enter to continue")

	def create_SG():
		name=input("Enter name of Security Group: ")
		desc=input("Enter description for Security Group: ")
		os.system('aws ec2 create-security-group --group-name {}  --description {}'.format(name,desc))
		input("\nPress enter to continue")

	def web_dist_Cf():
		name=input("Enter S3 bucket name to make it origin: ")
		os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(name))
		input("\nPress enter to continue")

					
	
	while True:
		os.system("tput setaf 3")
		print("\t\t\t----------------------------\n\t\t\t     Welcome to AWS menu\n\t\t\t----------------------------")
                                  
                               
		os.system("tput setaf 6")
		print("""\n\n\t\t
			1:To describe instances
			2:To launch instance
			3:To describe key-pair
			4:To create key-pair
			5:To create S3 bucket
			6:To transfer file from/to S3 bucket
			7:To create EBS volume
			8:To create Security-Group
			9:To configure web-distribution on Cloudfront

			0:To Exit
                	""")
		os.system("tput setaf 7")
		aws=input("Enter your choice: ")
		if int(aws)==1:
			os.system('aws ec2 describe-instances')
			input("\nPress enter to continue")
		elif int(aws)==2:
			launch_inst()
		elif int(aws)==3:
			os.system('aws ec2 describe-key-pairs')
			input("\nPress enter to continue")
		elif int(aws)==4:
			create_key_pair()
		elif int(aws)==5:
			create_S3_bucket()
		elif int(aws)==6:
			transfer_S3()
		elif int(aws)==7:
			create_EBS()
		elif int(aws)==8:
			create_SG()
		elif int(aws)==9:
			web_dist_Cf()	
		elif int(aws)==10:
			create_IAM()	
		elif int(aws)==0:
			break;
		else:
			print("Wrong Input")
			input("\nPress enter to continue")

						
		os.system('clear')

			




										      												
												
												
												
												
												
							




