from ftplib import FTP
ftp=FTP('192.168.1.1') #FTP ID
ftp.login()
ftp.cwd("User/MiniProject/Code") #Where to put data


with open('signal_1.txt',"wt") as signal_1:
    signal_1.write(dens)
    signal_1.flush()

