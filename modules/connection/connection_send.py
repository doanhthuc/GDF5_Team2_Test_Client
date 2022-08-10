from network.socket.out_packet import OutPacket
from network import cmd_code

class CmdSendHandShake(OutPacket):
    def __init__(self):
        super().__init__()
        self.init_data(2)
        self.set_controller_id(0)
        self.set_cmd_id(cmd_code.HAND_SHAKE)


class CmdSendLogin(OutPacket):
    def __init__(self):
        super().__init__()
        self.init_data(2)
        self.set_cmd_id(cmd_code.USER_LOGIN)

        self.__user = ""

    def set_data(self, user):
        self.__user = user

    def put_data(self):
        self.put_string("")
        self.put_string(self.__user)
        print("user = ", self.__user)

class CmdSendLogout(OutPacket):
    def __init__(self):
        super().__init__()
        self.init_data(2)
        self.set_controller_id(0)
        self.set_cmd_id(cmd_code.USER_LOG_OUT)

class CmdSendPing(OutPacket):
    def __init__(self):
        super().__init__()
        self.init_data(2)
        self.set_controller_id(0)
        self.set_cmd_id(cmd_code.PING)