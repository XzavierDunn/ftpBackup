import os
import ftplib


def createFolder(ftp, name, showOutput):
    print(name)
    if showOutput:
        print("Creating", str(name))
    os.mkdir(name)


def createFile(ftp, location, file, showOutput):
    print(location)
    new = open(location, "wb+")
    if showOutput:
        print("Downloading", str(file))
    ftp.retrbinary("RETR " + file, new.write, 1024)


def recur(ftp, where, localWhere, showOutput):
    ftp.cwd(where)
    os.chdir(localWhere)
    struct = {}
    files = ftp.nlst()
    if files != [i for i in struct.keys()]:
        for file in files:
            try:
                ftp.cwd(file)
                createFolder(ftp, str(os.getcwd() + '\\' + file), showOutput)
                os.chdir(file)
                struct[file] = recur(ftp,
                                     str(ftp.pwd()), str(os.getcwd()), showOutput)
                ftp.cwd('../')
                os.chdir('..\\')
            except ftplib.error_perm:
                struct[file] = ''
                createFile(ftp, str(os.getcwd() + '\\' + file),
                           file, showOutput)
    return struct


def recurAlt(ftp, where, localWhere, showOutput):
    ftp.cwd(where)
    os.chdir(localWhere)
    struct = {}
    files = ftp.nlst()
    if files != [i for i in struct.keys()]:
        for file in files:
            try:
                ftp.cwd(file)
                createFolder(ftp, str(os.getcwd() + '/' + file), showOutput)
                os.chdir(file)
                struct[file] = recurAlt(ftp,
                                        str(ftp.pwd()), str(os.getcwd()), showOutput)
                ftp.cwd('../')
                os.chdir('../')
            except ftplib.error_perm:
                struct[file] = ''
                createFile(ftp, str(os.getcwd() + '/' + file),
                           file, showOutput)
    return struct
