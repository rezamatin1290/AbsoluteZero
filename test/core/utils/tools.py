import hashlib
import os
import random
import sys
import string
from datetime import datetime
from core.color import color

sys.path.extend(['/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gtk-2.0'])
from passlib.hash import pbkdf2_sha256
print(os.path.abspath("."))
def GetStartupPath(fname):
    """return parent directory for fname"""
    return os.path.dirname(os.path.abspath(fname))

def GetRandomString(length=6):
    s = string.ascii_letters + string.digits
    return "".join([random.choice(s) for x in range(length)])


def FileExists(fname):
    return True if os.path.exists(fname) else False

def CreateFolderIfNotExists(file):
    if not os.path.exists(file):
        os.makedirs(file)
        return True
    return False

def GetHashFromPassword(passw):
    return pbkdf2_sha256.encrypt(passw, rounds=200000, salt_size=16)


def VerifyPassword(passw, hash_):
    return pbkdf2_sha256.verify(passw, hash_)

def GetNewLogFileName():
    return datetime.now().strftime("%d_%m_%Y-%H_%M_%S.log")

def Confirm(prompt):
    sys.stdout.write(color.ReturnQuestion("{} (Y/n)".format(prompt)))
    choose = input('')
    if choose.lower() == "y":
        return True
    return False

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def mkdir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
    except:
        return False

