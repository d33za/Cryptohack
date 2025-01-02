text = "label"
result = ''.join(chr(ord(c) ^ 13) for c in text)
print(result)