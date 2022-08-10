from modules.base_module import BaseModule
from modules.connection.connection_receive import *
from modules.connection.connection_send import *
from network import cmd_code
from network import error_code

from common.logger import logger

from network.socket.out_packet import OutPacket
from network import cmd_code

class CmdSendCheat(OutPacket):
    def __init__(self, type, params):
        super().__init__()
        self.init_data(2)
        self.set_cmd_id(cmd_code.CHEAT_EVENT)
        self.__type = type
        self.__params = params

    def put_data(self):
        self.put_string(self.__type)
        self.put_byte(len(self.__params))
        for i in range(len(self.__params)):
            self.put_string(str(self.__params[i]))



class CheatModule(BaseModule):
    def __init__(self, connector):
        super().__init__(connector)

        self.set_range_cmd(12000, 12999)


    def on_listener(self, cmd_id, raw_pkg):
        print("cheat::on_listener - cmd = {}".format(cmd_id))
        #pkg = None
        #if cmd_id == cmd_code.CHEAT_EVENT:

    def send_cheat(self, cheat_type, params):
        self.send(CmdSendCheat(cheat_type, params))