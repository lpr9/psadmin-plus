from psadmin_plus.actions.action import Action
        
class Restart(Action):

    def __init__(self):
        super().__init__()

    def _app(self,domain):
        self._psadmin(["-c","shutdown","-d",domain])
        self._psadmin(["-c","boot","-d",domain])
        # TODO - parallel switch - self._psadmin(["-c","parallelboot","-d",domain])

    def _prcs(self,domain):
        self._psadmin(["-p","stop","-d",domain])
        self._psadmin(["-p","start","-d",domain])

    def _web(self,domain):
        self._psadmin(["-w","shutdown","-d",domain])
        self._psadmin(["-w","start","-d",domain])
        # TODO ${PS_CFG_HOME?}/webserv/#{domain}/bin/startPIA.sh
