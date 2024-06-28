#!/usr/bin/python3

"""UTF-8 Validation interview practice question"""


def validUTF8(data):
    """ method determines if given set of data is a valid UTF-8 encoding

      params: data = List[int]
      returns: True if valid, false otherwise
    """
    BITS_IN_A_BYTE = 8
    index_pos = 0
    data_len = len(data)
    while index_pos < data_len:
        no_of_bytes = 0
        for bit in range(BITS_IN_A_BYTE):
            """shift LSB to the MSB position and
               check for valid UTF-8 start bits
            """
            if data[index_pos] >> (7 - bit) & 1 == 1:
                no_of_bytes += 1
            else:
                break

        # If leading bits is 0, the format must be:
        # 110xxxxx, 1110xxxx or 11110xxx so 2, 3 or 4 bytes
        if no_of_bytes == 1 or no_of_bytes > 4:
            return False

        # Go to next byte
        index_pos += 1

        # check sunsequent bytes start with format: 10xxxxxx
        for _ in range(1, no_of_bytes):
            # Right shifting by 6 ensures valid byte formats
            # have 10 at the end which is equal to 2
            if index_pos >= data_len or data[index_pos] >> 6 != 2:
                return False
            index_pos += 1

    return True
