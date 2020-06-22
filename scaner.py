import paramiko
import getpass
import sys
import time
from datetime import datetime
from pyexcel_ods3 import save_data
from collections import OrderedDict


command = 'df -h'
user = 'user'
password = '12345678'
data = OrderedDict()
data.update({'Sheet1': [['дата сканирования', 'ip адрес','Состояние системы', 'mac адрес']]})
f = open('scanlog.txt', 'r+')


for i in range(40,100,1):
    ip = '172.19.228.' + str(i)
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
            time.sleep(2)
            ssh.send('df -h\n')
            time.sleep(1)
            result = ssh.recv(100000).decode('utf-8')
            ssh.send('ifconfig\n')
            time.sleep(1)
            result2 = ssh.recv(100000).decode('utf-8')
            print(result + '\n' + result2)
            
            f.write(datetime.now() + ' ' +  ip + ' ' + result + ' ' + result2 + '\n')
            f.write('=================================================================')
           
    except:
        print("Host {} not valid or not desctination".format(ip))
        continue

    f.close()