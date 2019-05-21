from kazoo.client import KazooClient
import string 
import smtplib
import os 
import time
from email.mime.multipart import MIMEMultipart
from emai.mime.text import MEMEText
from email.mime.image import MIMEImage

zklist = [('ip1',port1),('ip2',port2),('ip3',port3)]
namedict={'ip1':["gee00a1","0"],
          'ip2':["gee00a2","1"],
          'ip3':["gee00a3","2"]
        }

def IsAlive( ip,port,idnum,readonly=True ):
    zk = KazooClient( hosts='%s:%d'%(ip,port),read_only=readonly ) 
    try:
        zk.start()
    except:
        return False,False
    else;
        try:
            children = zk.get_children('/brokers/ids')
        except:
            zk.stop()
            return False,False
        if idnum in children:
            zk.stop()
            return True,True
        else:
            zk.stop()
            return True,False


def sendmail(state):

if __name__=="__main__":
    state = {"(True,False)":[],
             "(True,True)":[],
             "(False,False)":[]
            }
    
    for ip,port in zklist;
        state[ str(IsAlive(ip,port,namedict[ip][1])) ].append(ip)
    print state 
    
    if len(state["(True,True)"])==len(zklist):
        pass
    else:
        sendmail(state)
