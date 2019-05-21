#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import os

def rm_files(path,filename):


    now_time = datetime.datetime.now()
    b = now_time+datetime.timedelta(hours=(-1))
    lasthour = b.strftime('%m-%d-%H')

    # rename the log file by format ( timestamp_filename)
    os.rename( path+filename,path+str(lasthour)+'_%s' %filename )

    
    # sort the log list by modify time( new to last)
    loglist = os.listdir(path)
    loglist.sort( key = lambda x: os.path.getmtime(path+filename) if os.path.isfile(path+filename) else 0 )


    # remian 3 hour log
    if len(loglist) <3:
        pass
    else:
        for i in range( len(loglist)-3):
            os.remove(path+logist[i])

if __name__ == "__main__"
    path_file = [ ('/data/alog/','aaa.log'),('/data/blog/','bbb.log'),('/data/clog/','ccc.log') ]
    for i,j in path_file:
        rm_files(i,j)


