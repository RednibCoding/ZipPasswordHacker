
# Zip dictonary password hacker
# 03.12.2016
# Michael Binder
#
# Uses a dictonary ("passwords.txt") where the passwords are stored
# to hack the password of a zip file ("test.zip")
# it tries all passwords in the "passwords.txt" to hack the zip file
# try different password files if the "passwords.txt" does not contain the correct password
# you can get password files at https://wiki.skullsecurity.org/index.php?title=Passwords
# or just google for: dictonary password list or dictonary password files or Password dictionaries
# ore something like that



import zipfile
from multiprocessing.pool import ThreadPool


class MultiThread():
    __thread_pool = None

    @classmethod
    def begin(cls, max_threads):
        MultiThread.__thread_pool = ThreadPool(max_threads)

    @classmethod
    def end(cls):
        MultiThread.__thread_pool.close()
        MultiThread.__thread_pool.join()

    def __init__(self, target=None, args:tuple=()):
        self.__target = target
        self.__args = args

    def run(self):
        try:
            result = MultiThread.__thread_pool.apply_async(self.__target, args=self.__args)
            return result.get()
        except:
            pass


def dictionary_attack(zip_path, password_file_path):
    zipFile = zipfile.ZipFile(zip_path)
    passwords = open_password_file(password_file_path)
    MultiThread.begin(400)
    for pwd in passwords:
        t = MultiThread(target=extract, args=(zipFile, pwd))
        success = t.run()
        if success: return
    MultiThread.end()


def extract(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print("Success! Possible Password: " + pwd)
        return True
    except:
        return False

def open_password_file(password_file_path):
    with open(password_file_path, "r") as password_file:
        passwords = []
        for line in password_file:
            password = line.strip("\n")
            passwords.append(password)
    return passwords


dictionary_attack("test.zip", "passwords.txt")
input()
