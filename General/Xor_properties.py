# Helper function to perform XOR on hex strings
def hex_xor(hex1, hex2):
    # Convert hex strings to bytes
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)
    
    # XOR the bytes
    xored = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))
    
    return xored

# Given values from the challenge
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Solving for individual key values
key2 = hex_xor(key1_2, key1.hex())
key3 = hex_xor(key2.hex(), key2_3)

# Get the flag
flag = hex_xor(flag_key123, hex_xor(key1.hex(), hex_xor(key2.hex(), key3.hex()).hex()).hex())

# Print the decoded flag
print(flag.decode())