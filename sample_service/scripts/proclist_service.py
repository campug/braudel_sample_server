import sys, os
import win32serviceutil, win32service

class ProcessListService(win32serviceutil.ServiceFramework):

    _svc_name_         = "SampleProcListService"
    _svc_display_name_ = "Sample Process List Service"
    _svc_description_  = "Sample xmlrpc service to list running processes"

    def SvcDoRun(self):
        ''' run the xmlrpc server
        '''
        from twisted.web import server
        from twisted.internet import reactor
        from sample_service.rpc import WinRPC
    
        r = WinRPC()
        reactor.listenTCP(7080, server.Site(r))
        reactor.run(installSignalHandlers=0)

    def SvcStop(self):
        ''' stop the rpc server
        '''
        # notify Service Control Manager that we are still shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # get a handle to reactor in this thread and stop
        from twisted.internet import reactor
        reactor.stop()


if __name__ == '__main__':
    ''' 
    usage:
        proclist_service.py install/remove
        proclist_service.py start/stop/restart
    '''
    for index, value in enumerate(sys.argv):
        # correct -install/-remove from bdist_msi
        # install/remove steps into "non-dash counterparts" 
        # required by win32serviceutil
        if value == '-install':
            sys.argv[index] = '--startup=auto'
            sys.argv.insert(index + 1, 'install')
            
        elif value == '-remove':
            sys.argv[index] = 'remove'

    win32serviceutil.HandleCommandLine(ProcessListService)
