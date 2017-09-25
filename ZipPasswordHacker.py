
# Zip dictonary password hacker
# 03.12.2016
# Michael Frank
#
# Uses a dictonary ("passwords.txt") where the passwords are stored
# to hack the password of a zip file ("test.zip")
# it tries all passwords in the "passwords.txt" to hack the zip file
# try different password files if the "passwords.txt" does not contain the correct password
# you can get password files at https://wiki.skullsecurity.org/index.php?title=Passwords
# or just google for: dictonary password list or dictonary password files or Password dictionaries
# ore something like that



import zipfile
import itertools
import string
import traceback
from threading import Thread


zipFile = zipfile.ZipFile("test.zip") # the zip file you want to crack


def dictionary():
    passwords = open("passwords.txt") # The txt file where the passwords are stored to check
    for line in passwords.readlines():
        pwd = line.strip("\n")
        t = Thread(target = crack, args = (zipFile, pwd))
        t.start()
        

def bruteforce():
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(3,10):
        for j in map("".join, itertools.product(myLetters, repeat=i)):
            t = Thread(target = crack, args = (zipFile, j))
            t.start()


def crack(zip, pwd):
    try:
        zip.extractall(pwd = str.encode(pwd))
        print("Success: Posssible Password is " + pwd)
    except:
        pass

dictionary()
input()
