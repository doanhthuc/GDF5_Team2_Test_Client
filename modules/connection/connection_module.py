
from modules.base_module import BaseModule
from modules.connection.connection_receive import *
from modules.connection.connection_send import *
from network import cmd_code
from network import error_code

from common.logger import logger


class ConnectionModule(BaseModule):
    def __init__(self, connector):
        super().__init__(connector)

        self.set_range_cmd(0, 1000)

        self.__session_token = ""

        self.__login_code = -1
        self.__session_key = ""

    def on_listener(self, cmd_id, raw_pkg):
        print("connection_module::on_listener - cmd = {}".format(cmd_id))
        pkg = None
        if cmd_id == cmd_code.HAND_SHAKE:
            pkg = CmdReceiveHandShake()
            pkg.init(raw_pkg)
            self.on_process_hand_shake(pkg)

        elif cmd_id == cmd_code.USER_LOGIN:
            pkg = CmdReceiveLogin()
            pkg.init(raw_pkg)
            self.on_process_login(pkg)

        #elif

    def on_process_hand_shake(self, pkg):
        self.__session_token = pkg.get_session_token()
        print("connection_module::on_process_hand_shake - ss token: >>{}<<".format(self.__session_token))
        self.send_login()

    def get_login_code(self):
        print("get_login_code self {} ".format(self.__login_code))
        return self.__login_code

    def on_process_login(self, pkg):
        error = pkg.get_error()
        print("check login ok {}".format(error))
        self.__login_code = error

        if error == error_code.SUCCESS:
            logger.info("connect success")

        elif error == error_code.SESSION_EXPIRED or error == error_code.SESSION_KEY_INVALID:
            logger.error("error 2")

    def send_login(self):
        print("connection_module::send_login ssk = {}".format(self.__session_key))
        packet = CmdSendLogin()

        packet.set_data(self.__session_key)
        self.send(packet)

    def send_log_out(self):
        packet = CmdSendLogout()
        self.send(packet)

    def set_session_key(self, ssk):
        self.__session_key = ssk

    def connect(self, user_name, password):
        self.set_session_key(user_name)

        pk = CmdSendHandShake()
        self.send(pk)


