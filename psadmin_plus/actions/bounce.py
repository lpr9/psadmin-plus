from psadmin_plus.actions.action import Action
        
class Bounce(Action):

    def __init__(self):
        super().__init__()

    def _app(self,domain):
        self._psadmin(["-c","shutdown","-d",domain])
        self._psadmin(["-c","purge","-d",domain])
        self._psadmin(["-c","cleanipc","-d",domain])
        self._psadmin(["-c","configure","-d",domain])
        self._psadmin(["-c","boot","-d",domain])
        # TODO - parallel switch - self._psadmin(["-c","parallelboot","-d",domain])

    def _prcs(self,domain):
        self._psadmin(["-p","stop","-d",domain])
        print('prcs purge coming soon! - TODO')
        self._psadmin(["-p","cleanipc","-d",domain])
        self._psadmin(["-p","configure","-d",domain])
        self._psadmin(["-p","start","-d",domain])

    def _web(self,domain):
        self._psadmin(["-w","shutdown","-d",domain])
        print('web purge coming soon! - TODO')
        self._psadmin(["-w","start","-d",domain])
        # TODO ${PS_CFG_HOME?}/webserv/#{domain}/bin/startPIA.sh
