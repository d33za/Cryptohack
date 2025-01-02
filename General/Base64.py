from base64 import *

flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

flag = bytes.fromhex(flag)
print(b64encode(flag))