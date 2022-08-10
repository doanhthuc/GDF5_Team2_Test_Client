from network.socket.out_packet import OutPacket

class CmdCommonPacket(OutPacket):
    def __init__(self, cmd_id):
        super().__init__()
        self.init_data(2)
        self.set_cmd_id(cmd_id)

