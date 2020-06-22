import paramiko
import getpass
import sys
import time
from datetime import datetime

user = 'user'
password = '12345678'
f = open('Gracheva12D.txt', 'w')

for i in range(1,254,1):
        ip = '172.23.79.' + str(i)
        print("Connecting to {}".format(ip))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(
            hostname = ip,
            username = user,
            password = password,
            look_for_keys=False,
            allow_agent=False
            )   
    
            with client.invoke_shell() as ssh:
                time.sleep(0.4)
                ssh.send('df -h\n')
                filesystem = ssh.recv(5000).decode('utf-8')
                ssh.send('ifconfig\n')
                time.sleep(0.5)
                ssh.send('su\n')
                ssh.send('000000\n')
                ssh.send('yum clean all\n')
                ifconfig = ssh.recv(5000).decode('utf-8')
                f.write(str(datetime.now()) + ' ' + ip + ' ' + filesystem + ' ' + ifconfig + '\n' + '==========================================\n')
                print(filesystem + '\n' + ifconfig)
                
        except Exception as ex:
            f.write(str(ex) + '\n' + '==========================================\n')
            print(str(ex))
            continue
        
f.close()