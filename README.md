# GMAIL PASSWORD CRACKER
This project has two files, **cracker.py**, which cracks passwords, and **passwords.txt**, which contains passwords. Ask the person who's password you are trying to crack to enter a bunch of passwords to **passwords.txt**. Run the **cracker.py** script and do what it asks and the password should be cracked.

# Requirements
**Python**

**smtplib**:
```bash
$ pip install smtplib
```
**termcolor**:
```bash
$ pip install termcolor
```

# Useage
Run the following commands:
On **Mac**:
```bash
python3 /path/to/file
```
On **Windows**:
```bash
py C:\path\to\file
```


# Issue
Gmail has a security block that prevents scripts and code to login in emails or try to get passwords. In order to fix this, navigate to "https://myaccount.google.com/u/0/?hl=en", and go to **Security**. Scroll towards the bottom and at **Less secure app access**, enable the feature. Google does not recommend this but this is perfectly safe as long as the **passwords.txt** file and your friends email do not get passed around everywhere.