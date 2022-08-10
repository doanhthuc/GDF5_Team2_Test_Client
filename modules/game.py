from network.socket.zps_client import ZPSClient
from modules.connection.connection_module import ConnectionModule
from modules.player.player_module import PlayerModule
from modules.cheat.cheat_module import CheatModule

class Game:

    def __init__(self):
        print("game::init - init game")
        self.__connector = ZPSClient()
        self.__connector.start()

        self.__connection_module = ConnectionModule(self.__connector)
        self.__player_module = PlayerModule(self.__connector)
        self.__cheat_module = CheatModule(self.__connector)

        self.__connector.add_module(self.__connection_module)
        self.__connector.add_module(self.__player_module)
        self.__connector.add_module(self.__cheat_module)

    def get_connector(self):
        return self.__connector

    def get_connection_module(self):
        return self.__connection_module

    def get_player_module(self):
        return self.__player_module

    def get_cheat_module(self):
        return self.__cheat_module

    #--------------

    def login(self, user_name, password):
        self.__connection_module.connect(user_name, password)

    def logout(self):
        self.__connection_module.send_log_out()

    def get_login_code(self):
        return self.__connection_module.get_login_code()

    def get_player_name(self):
        return self.__player_module.get_player_name()

    def get_uId(self):
        return self.__player_module.get_uId();


