import os
import click
import shutil
import ftplib
from src.service import createFolder, createFile, recur


@click.command()
@click.option('--directory', default='/home/minecraft/server/world', help='The directory you would like to download from the FTP server. Default: /home/minecraft/server/world')
@click.option('--local', default='world', help='The local folder everything will download to. Default: world')
@click.option('--username', default='', help='FTP username')
@click.option('--password', default='', help='FTP password')
@click.option('--host', default='', help='FTP host (IP)')
@click.option('--passive', default=False, help='FTP passive toggle. Default: False')
@click.option('--output', default=True, help='Display which files are being downloaded/created.')
def main(directory, local, username, password, host, passive, output):
    print("I recommend you turn your server off before you begin.\nFiles like the 'session.lock' don't always play nicely.")
    x = input('Continue? y/n >')
    if x.lower() == 'y':
        # Check OS create seperate logic for mac/linux # os.chmod(local, 0o777) ## needed for mac/linux ?

        # Create / recreate the local directory
        if os.path.exists(local):
            shutil.rmtree(local)
            os.mkdir(local)
        else:
            os.mkdir(local)

        # Connect to FTP
        with ftplib.FTP(host) as ftp:
            try:
                ftp.login(username, password)
                ftp.set_pasv(passive)
                recur(ftp, directory, str(os.getcwd() + '\\' + local), output)
            except ftplib.error_perm:
                print(
                    f'FTP login failed, Your username: {username} or password: {password} is incorrect.')
    print('\nFinished')


if __name__ == '__main__':
    main()
