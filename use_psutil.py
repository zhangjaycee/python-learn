#!/usr/bin/python

import psutil

###CPU###

#print "cpu_times():",psutil.cpu_times()
print "cpu_count():(logical)",psutil.cpu_count()# logical
print "cpu_count():(physical)",psutil.cpu_count(logical = False)# physical


###MEMORY###

mem = psutil.virtual_memory()
#print mem
print "total mem:",mem.total
print "swap:",psutil.swap_memory()

###PROCESS###

#print psutil.pids()
p = psutil.Process(690)
print p.name(),"p.name()"
print p.exe(),"p.exe()"
#print p.cwd(),"p.cwd()" #need sudo
#print p.connections(),"p.connections()"

###POPEN###

from subprocess import PIPE
p = psutil.Popen(["python", "-c", "print('hello')"], stdout= PIPE)
print p.name()
print p.username()
print p.communicate()
