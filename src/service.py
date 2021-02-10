import os
import ftplib
from ftplib import FTP


def createFolder(name, print=False):
    if print:
        print("Creating", str(name))
    os.mkdir(name)


def createFile(location, file, print=False):
    new = open(location, "wb+")
    if print:
        print("Downloading", str(file))
    ftp.retrbinary("RETR " + file, new.write, 1024)


def recur(where, localWhere, print=False):
    ftp.cwd(where)
    os.chdir(localWhere)
    struct = {}
    files = ftp.nlst()
    if files != [i for i in struct.keys()]:
        for file in files:
            try:
                ftp.cwd(file)
                createFolder(str(os.getcwd() + '\\' + file))
                os.chdir(file)
                struct[file] = recur(
                    str(ftp.pwd()), str(os.getcwd()), print=print)
                ftp.cwd('../')
                os.chdir('..\\')
            except ftplib.error_perm:
                struct[file] = ''
                createFile(str(os.getcwd() + '\\' + file), file)
    return struct
