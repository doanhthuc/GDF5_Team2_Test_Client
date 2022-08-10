from network.socket.in_packet import InPacket

class CmdReceiveHandShake(InPacket):
    def __init__(self):
        super().__init__()
        self.__sessionToken = ""

    def read_data(self):
        self.__sessionToken = self.get_string()

    def get_session_token(self):
        return self.__sessionToken

class CmdReceiveLogin(InPacket):
    def __init__(self):
        super().__init__()