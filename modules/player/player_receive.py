from network.socket.in_packet import InPacket

class CmdReceivePlayerInfo(InPacket):
    def __init__(self):
        super().__init__()

    def read_data(self):
        self.uId = self.get_int()
        self.displayName = self.get_string()
        #self.displayName = self.get_string()
        self.gold = self.get_int()

        self.gem = self.get_int()
        self.trophy = self.get_int()
        self.timeServer = self.get_long()

        print("uid = {}".format(self.uId))
        print("displayName = {}".format(self.displayName))
        print("gold = {}".format(self.gold))
        print("gem = {}".format(self.gem))
        print("trophy = {}".format(self.trophy))
        print("timeServer = {}".format(self.timeServer))
