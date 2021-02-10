import os
import click
import shutil

from src.service import createFolder, createFile, recur


@click.command()
@click.option('--directory', default='/home/minecraft/server/world', help='The directory you would like to download from the FTP server.')
@click.option('--local', default='/world', help='The local folder everything will download to.')
@click.option('--username', default='', help='FTP username')
@click.option('--password', default='', help='FTP password')
@click.option('--host', default='', help='FTP host (IP)')
@click.option('--passive', default=False, help='FTP passive toggle')
# @click.option('--port', default='21', help='FTP port')
# @click.option('--timeout', default=20, help='FTP timeout')
#
#
#
def main(directory, local, username, password, host, port, passive, timeout):
    # Create / recreate the local directory
    if os.path.exists(local):
        shutil.rmtree(local)
        os.mkdir(local)
    else:
        os.mkdir(local)

    # Connect to FTP
    with FTP(host) as ftp:
        print('Login? =>', ftp.login(user, passwd))
        ftp.set_pasv(passive)
        recur(directory, str(os.getcwd() + local))


if __name__ == '__main__':
    main()
