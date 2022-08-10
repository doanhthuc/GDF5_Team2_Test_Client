

BIT_IS_BINARY_INDEX = 7
BIT_IS_ENCRYPT_INDEX = 6
BIT_IS_COMPRESS_INDEX = 5
BIT_IS_BLUE_BOXED_INDEX = 4
BIT_IS_BIG_SIZE_INDEX = 3

BYTE_PACKET_SIZE_INDEX = 1
BIG_HEADER_SIZE = 5
NORMAL_HEADER_SIZE = 3
INDEX_SIZE_PACKET = 1


def get_bit(i_input, index):
    result = i_input & (1 << index)
    return result != 0

def set_bit(i_input, index, has_bit):
    if has_bit:
        i_input |= 1 << index
    else:
        i_input &= ~(1 << index)

    return i_input

def get_int_at(data, index):
    return ((data[index] & 255) << 24) + \
        ((data[index + 1] & 255) << 16) + \
        ((data[index + 2] & 255) << 8) + \
        ((data[index + 3] & 255) << 0)

def get_unsigned_short_at(data, index):
    a = (data[index] & 255) << 8
    b = (data[index + 1] & 255) << 0
    return a + b

def get_short_at(data, index):
    return (data[index] << 8) + (data[index + 1] & 255)

def get_cmd_id_from_data(data):
    return get_short_at(data, 1)

def is_big_size(data):
    return get_bit(data[0], BIT_IS_BIG_SIZE_INDEX)

def is_compress(data):
    return get_bit(data[0], BIT_IS_COMPRESS_INDEX)

def gen_header(big_size, compress):
    header = 0
    header = set_bit(header, BIT_IS_BINARY_INDEX, True)
    header = set_bit(header, BIT_IS_ENCRYPT_INDEX, False)
    header = set_bit(header, BIT_IS_COMPRESS_INDEX, compress)
    header = set_bit(header, BIT_IS_BLUE_BOXED_INDEX, True)
    header = set_bit(header, BIT_IS_BIG_SIZE_INDEX, big_size)
    return header

def get_valid_size(data, length):
    big_size = is_big_size(data)
    data_size = 0
    add_size = 0
    if big_size:
        if length < BIG_HEADER_SIZE:
            return -1
        data_size = get_int_at(data, BYTE_PACKET_SIZE_INDEX)
        add_size = BIG_HEADER_SIZE

    else:
        if length < NORMAL_HEADER_SIZE:
            return -1
        data_size = get_unsigned_short_at(data, BYTE_PACKET_SIZE_INDEX)
        add_size = NORMAL_HEADER_SIZE

    return data_size + add_size

def get_data_size(data):
    big_size = is_big_size(data)
    if big_size:
        return get_int_at(data, BYTE_PACKET_SIZE_INDEX)
    else:
        return get_unsigned_short_at(data, BYTE_PACKET_SIZE_INDEX)

class PacketHeaderAnalyze():
    def __init__(self):
        super().__init__()



