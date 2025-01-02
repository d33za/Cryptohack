
data = bytes.fromhex('73626960647f6b206821204f2125447d694f7624662065622127234726927756d')

for i in range(256):
   result = ''.join(chr(b ^ i) for b in data)
   if 'crypto' in result:
       print(result)
       break