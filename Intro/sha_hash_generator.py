from passlib.hash import sha1_crypt, sha256_crypt, sha512_crypt

passwords = ["changeme", "password", "123456"]
salt = ["8sFt66rZ"]

for password in passwords:
    sha1_hash = sha1_crypt.encrypt(password, salt=salt)
    sha256_hash = sha256_crypt.encrypt(password, salt=salt)
    sha512_hash = sha512_crypt.encrypt(password, salt=salt)

    print(f'Password: {password}')
    print(f'SHA1: {sha1_hash}')
    print(f'SHA256: {sha256_hash}')
    print(f'SHA512L {sha512_hash}')
    print()