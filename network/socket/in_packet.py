import struct
from network.socket.packet_header_analyze import *
from network import error_code

class InPacket():

    def __init__(self):
        #self.__capacity = None
        self.__data = None
        self.__controller_id = None
        self.__cmd_id = None
        #self.__is_packed_header = False
        self.__length = None
        self.__pos = None
        self.__error = None

    def init(self, pkg):
        #self.process(pkg)
        # debug parse byte

        self.__pos = 0
        self.__data = pkg.get_data()
        self.__length = pkg.get_data_size()

        self.__controller_id = self.parse_byte()
        self.__cmd_id = self.get_short()
        self.__error = self.parse_byte()

        if self.__error == error_code.SUCCESS:
            self.read_data()

    def process(self, pkg):
        # analyze raw pkg
        valid_size = get_valid_size(pkg, 1024)
        if valid_size < 0 or valid_size > len(pkg):
            print("error invalid package size")
            return

        # process package
        size = get_data_size(pkg)
        temp_buffer = bytearray(0)
        for i in range(size):
            temp_buffer.append(pkg[i])
            print(pkg[i])

        self.__data = temp_buffer
        self.__length = len(temp_buffer)

        print("size buffer = {}".format(temp_buffer))

    def get_error(self):
        return self.__error

    def get_data(self):
        return self.__data

    def get_controller_id(self):
        return self.__controller_id

    def get_cmd_id(self):
        return self.__cmd_id

    def parse_byte(self):
        res = int.from_bytes(self.__data[self.__pos:self.__pos + 1], byteorder='big', signed=True)
        #print("in_packet::self.parse_byte - pos = {}, b = {}".format(self.__pos, res))
        self.__pos = self.__pos + 1
        return res

    def get_byte(self):
        return self.parse_byte()

    def get_bool(self):
        return self.parse_byte() > 0

    def get_bytes(self, size):
        #print("pos = {}, size = {}, length = {}".format(self.__pos, size, self.__length))
        assert self.__pos + size <= self.__length, "IndexOutOfBoundsException - get_bytes"
        data = bytearray(size)
        for i in range(size):
            data[i] = self.parse_byte()

        return data

    def get_int(self):
        assert self.__pos + 4 <= self.__length, "IndexOutOfBoundsException - get_int"
        res = int.from_bytes(self.__data[self.__pos:self.__pos + 4], byteorder='big', signed=True)
        self.__pos = self.__pos + 4
        return res

    def get_short(self):
        assert self.__pos + 2 <= self.__length, "IndexOutOfBoundsException - get_short"
        res = int.from_bytes(self.__data[self.__pos:self.__pos + 2], byteorder='big', signed=True)
        self.__pos = self.__pos + 2
        return res

    def get_unsigned_short(self):
        assert self.__pos + 2 <= self.__length, "IndexOutOfBoundsException - get_unsigned_short"
        a = (self.parse_byte() & 255) << 8
        b = (self.parse_byte() & 255) << 0
        return a + b

    def get_char_array(self, size):
        size[0] = self.get_unsigned_short()
        #print("in_packet::get_char_array - size = {}".format(size[0]))
        return self.get_bytes(size[0])

    def get_string(self):
        size = [0]
        #print("size get_string = {}".format(size[0]))
        out = self.get_char_array(size)
        result = "".join(map(chr, out))
        return result

    def get_long(self):
        assert self.__pos + 8 <= self.__length, "IndexOutOfBoundsException - get_long"
        res = int.from_bytes(self.__data[self.__pos:self.__pos + 8], byteorder='big', signed=True)
        self.__pos = self.__pos + 8
        return res

    def get_float(self):
        # >f: big edian
        # <f: little edian
        res = struct.unpack('>f', self.__data[self.__pos:self.__pos + 4])
        self.__pos = self.__pos + 4
        return res

    def get_double(self):
        res = struct.unpack('>d', self.__data[self.__pos:self.__pos + 8])
        self.__pos = self.__pos + 8
        return res

    def read_data(self):
        pass
        #result = self.get_string()
        #print("check result: >>{}<<".format(result))








