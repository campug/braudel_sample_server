#!c:\python27\python.exe

from xmlrpclib import ServerProxy

wmi = ServerProxy('http://127.0.0.1:7080')
for process in wmi.running():
    print "%40s %s" % (process['name'], process['path'])

