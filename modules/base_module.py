

class BaseModule:

    def __init__(self, connector):
        #
        self.__connector = connector
        self.__min_cmd = -1
        self.__max_cmd = -1

    def set_range_cmd(self, min_x, max_x):
        self.__min_cmd = min_x
        self.__max_cmd = max_x

    def get_min_cmd(self):
        return self.__min_cmd

    def get_max_cmd(self):
        return self.__max_cmd

    def get_connector(self):
        return self.__connector

    def send(self, pkg):
        self.get_connector().send(pkg)

    def is_in_range_listener(self, cmd_id):
        return self.__min_cmd <= cmd_id <= self.__max_cmd

    def on_listener(self, cmd_id, raw_pkg):
        # override me
        print("on_listener {}".format(cmd_id))