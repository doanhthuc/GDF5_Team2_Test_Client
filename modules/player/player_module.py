from modules.base_module import BaseModule
from modules.player.player_send import CmdSendOpenChest
from network.base_packet import *
from network import cmd_code, error_code
from modules.player.player_receive import *

from common.logger import logger

class PlayerModule(BaseModule):

    def __init__(self, connector):
        super().__init__(connector)

        self.set_range_cmd(1001, 4999)

        self.__player_name = ""
        self.__uId = -1

    def on_listener(self, cmd_id, raw_pkg):
        pkg = None
        if cmd_id == cmd_code.PLAYER_GET_INFO:
            pkg = CmdReceivePlayerInfo()
            pkg.init(raw_pkg)
            self.on_process_player_info(pkg)
        if cmd_id == cmd_code.OPEN_CHEST:
            pkg = CmdReceiveOpenChest()
            pkg.init(raw_pkg)
            self.on_process_open_chest(pkg)


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
    
    def send_open_chest(self, chestId):
        pkg = CmdSendOpenChest()
        pkg.set_data(chestId)
        self.send(pkg)

    def on_process_open_chest(self, pkg):
        error = pkg.get_error()
        print("check open chest ok {}".format(error))
        self.__open_chest_code = error

        if error == error_code.SUCCESS:
            logger.info("connect success")

    def get_open_chest_code(self):
        return self.__open_chest_code

