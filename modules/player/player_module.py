from modules.base_module import BaseModule
from network.base_packet import *
from network import cmd_code
from modules.player.player_receive import *

class PlayerModule(BaseModule):

    def __init__(self, connector):
        super().__init__(connector)

        self.set_range_cmd(1001, 1149)

        self.__player_name = ""
        self.__uId = -1

    def on_listener(self, cmd_id, raw_pkg):
        pkg = None
        if cmd_id == cmd_code.PLAYER_GET_INFO:
            pkg = CmdReceivePlayerInfo()
            pkg.init(raw_pkg)
            self.on_process_player_info(pkg)

    def send_get_player_info(self):
        pk = CmdCommonPacket(cmd_code.PLAYER_GET_INFO)
        self.send(pk)

    def on_process_player_info(self, pkg):
        self.__player_name = pkg.displayName
        self.__uId = pkg.uId

    def get_player_name(self):
        return self.__player_name

    def get_uId(self):
        return self.__uId

