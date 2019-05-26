from kazoo.client import KazooClient
import string 
import os 
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from emai.mime.text import MEMEText
from email.mime.image import MIMEImage

zkList = [('ip1',port1), ('ip2',port2), ('ip3',port3)]
nameDict={'ip1':["g00a1","0"],
          'ip2':["g00a2","1"],
          'ip3':["g00a3","2"]
        }

def IsAlive( ip, port, idnum, readonly=True ):
    zk = KazooClient( hosts='%s:%d' %(ip,port), read_only=readonly ) 
    try:
        zk.start()
    except:
        return False, False 
    else:
        try:
            children = zk.get_children('/brokers/ids')
        except:
            zk.stop()
            return False, False
        if idnum in children:
            zk.stop()
            return True, True
        else:
            zk.stop()
            return True, False


def sendmail(state):
    pass

if __name__=="__main__":
    state = {"(True,False)":[], # zookeeper alive, idnum none
             "(True,True)":[],  # zookeeper alive, idnum exists
             "(False,False)":[] # zookeeper dead, idnum none
            }
    
    for ip,port in zkList;
        state[ str(IsAlive(ip, port, nameDict[ip][1])) ].append(ip)
    print state 
    
    if len(state["(True,True)"]) == len(zkList):
        pass
    else:
        sendmail(state)
