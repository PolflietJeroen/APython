#!/usr/bin env python3

from collections import namedtuple
import argparse
import struct
import os

parser = argparse.ArgumentParser()
parser.add_argument('zipfile', type=argparse.FileType('rb'))
args = parser.parse_args()

class ZipHeader(namedtuple('ZipHeader', 'header, version, general_purpose, compression_method, file_last_modification_date, file_last_modification_time, crc32, compressed_size, uncompressed_size    , file_name_length, extra_field_length')):
    def __new__(cls, data):
        assert len(data) == 11, "I'm expecting 11 elements of data"
        expected_sig = 0x04034b50
        assert data[0] == expected_sig, "I'm expecting local file header signature of {:X}, but got {:X}".format(expected_sig, data[0])
        return super(ZipHeader, cls).__new__(cls, *data)
    
f = args.zipfile # lazynes

while True: 
    header = f.read(30)
    unpacked_header = struct.unpack('<IHHHHHIIIHH', header)
    
    if unpacked_header[0] == 0x02014b50: 
        break
        
    zh = ZipHeader(unpacked_header)
    
    name = f.read(zh.file_name_length)
    name = name.decode() 
    
    extra = f.read(zh.extra_field_length)
    f.seek(zh.compressed_size, os.SEEK_CUR)
    
    print("Found file {}; Compressed: {}; Uncompressed: {}".format(name, zh.compressed_size, zh.uncompressed_size))

