from pwn import xor

k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k21 = bytes.fromhex('37dcb2920301aa90d07eae17e3b1c6d8daf94c35d4c9191a5e1e')
k23 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf01d6ddde5fc1')
flag = bytes.fromhex('0d4e9855208a2cd59091d04767ae47963170d1660df7f56f5fa1')

k3 = xor(k1, k21, k23)

result = xor(flag, k1, k21, k3)
print(result)