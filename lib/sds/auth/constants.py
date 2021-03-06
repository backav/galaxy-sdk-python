# encoding: utf-8
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from .ttypes import *

SIGNATURE_SUPPORT = {
    1 : False,
    2 : True,
    10 : True,
    11 : True,
    12 : False,
    13 : False,
}
HK_AUTHORIZATION = "Authorization"
HK_HOST = "Host"
HK_TIMESTAMP = "X-Xiaomi-Timestamp"
HK_CONTENT_MD5 = "X-Xiaomi-Content-MD5"
HK_VERSION = "X-Xiaomi-Version"
HK_USER_TYPE = "X-Xiaomi-User-Type"
HK_SECRET_KEY_ID = "X-Xiaomi-Secret-Key-Id"
HK_SECRET_KEY = "X-Xiaomi-Secret-Key"
HK_SIGNATURE = "X-Xiaomi-Signature"
HK_MAC_ALGORITHM = "X-Xiaomi-Mac-Algorithm"
HK_SUPPORT_ACCOUNT_KEY = "X-Xiaomi-Support-Account-Key"
SUGGESTED_SIGNATURE_HEADERS = [
  "Host",
  "X-Xiaomi-Timestamp",
  "X-Xiaomi-Content-MD5",
]
