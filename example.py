from getpass import getpass
import time
import os
import shutil
import logging
import liucAPI as LIUC


#this is a simple example of liucAPI library implementation

print("Insert your username: (ex: pi53.rossi)")
username = input()
print("Insert your password: ")
pwd = getpass()

print(LIUC.login(username, pwd))
print(LIUC.get_libretto(username, pwd))
print(LIUC.get_media(username, pwd))
LIUC.liucLogin(username, pwd)
print(LIUC.get_last_mark(username, pwd))

