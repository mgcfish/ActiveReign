class ExampleModule():
    def __init__(self):
        self.name           = 'Example Module'
        self.description    = 'Will take in CMD arg and print to screen'
        self.author         = ['@m8r0wn']
        self.requires_admin = False
        self.supported_exec_methods   = ['wmiexec', 'smbexec', 'atexec', 'winrm', 'ssh']
        self.args = {
            'ARGUMENTS': {
                'Description'   : 'Value to print',
                'Required'      : False,
                'Value'         : 'Default Value!'
            }
        }


    """
    
    Class methods here as needed
    
    """

    def run(self, target, args, smb_con, loggers, config_obj):
        """
        Each module is executed from self.run, and passed the following arguments:

        target  - Current target in enumration process
        args    - Command line args
        smb_con - Active SMB Connection
        loggers - Dictionary of queues used to output data
          loggers['console'] - Write data to terminal
          loggers['enum']     - Write data to log file enum.csv

        Once Complete, Add the module to the _Modules dictionary in ar3.modules.__init__.py
        """
        loggers['console'].success([smb_con.host, smb_con.ip, self.name.upper(),"Example Module Output: {}".format(self.args['ARGUMENTS']['Value'])])
