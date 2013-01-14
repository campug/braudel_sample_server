from twisted.web import xmlrpc
from wmi import WMI
wmiHandle = WMI()

class WinRPC(xmlrpc.XMLRPC):
    """
    Sample xmlrpc resource to list running processes
    in win32 over xmlrpc
    """

    def xmlrpc_running(self):
        """
        Return all running processes.
        """
        return [{
            'id':     process.ProcessId,
            'status': process.Status or 'N/A',
            'name':   process.Name,
            'path':   process.ExecutablePath or 'N/A'
            } 
            for process in wmiHandle.Win32_Process()]
    
    xmlrpc_running.signature = [['array']]
        
