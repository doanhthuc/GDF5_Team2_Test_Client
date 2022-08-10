from network.socket.packet_header_analyze import *

class RawPacket:
    def __init__(self):
        self.__size = 0
        self.__data = None
        self.__result = None

    def get_data(self):
        return self.__data

    def get_data_size(self):
        return self.__size

    def process(self, buff, size):
        data_size = get_data_size(buff)
        compress = is_compress(buff)
        big_size = is_big_size(buff)

        #print("RAW_PACKET - process check {} {} {}".format(data_size, compress, big_size))

        header_size = NORMAL_HEADER_SIZE
        if big_size:
            header_size = BIG_HEADER_SIZE

        self.__data = bytearray(0)
        if compress:
            print("AAAAAAAAAAAAAAAAA")
        else:
            for i in range(data_size):
                self.__data.append(0)

            for i in range(data_size):
                #print("check index {} = {}".format(i, buff[i + header_size]))
                self.__data[i] = buff[i + header_size]

        self.__size = data_size
        #print("RAW_PACKET: size = {}".format(self.__size))
        #for i in range(len(self.__data)):
        #    print(self.__data[i], end=",")

        return True
