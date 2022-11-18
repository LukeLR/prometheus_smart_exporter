import contextlib
import logging
import pathlib
import re
import subprocess
import struct
import socket
import sys

DEVICE_PATH_PATTERN = re.compile(
    r"([0-9]+:){3}[0-9]+"
)

def iter_drives():
    base = pathlib.Path("/sys/bus/scsi/devices/")
    for p in base.iterdir():
        basename = p.parts[-1]
        if DEVICE_PATH_PATTERN.match(basename):
            if (p / "block").is_dir():
                
                for blockdev in (p / "block").iterdir():
                    yield basename, blockdev.parts[-1]
                    
def main():
    print("yo")
    import argparse
    x = iter_drives()
    print("world")
    print(x)
    print(iter_drives())




#for port, device in iter_drives():
#    print(device)

import os
import os.path
import string
print('hello')
x = 'sd' + e for e in string.ascii_lowercase if not os.path.exists('/dev/sd' + e)
print('world')