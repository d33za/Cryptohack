from passlib.hash import apr_md5_crypt

# Function to create APR1 hash
def create_apr1_hash(password, salt):
    return apr_md5_crypt.encrypt(password, salt=salt)

# Define the passwords and the salt
passwords = ["changeme", "123456", "password"]
salt = "PkWj6gM4"  # Using the same salt for all for this example

# Generate and print the APR1 hashes
for password in passwords:
    hashed_password = create_apr1_hash(password, salt)
    print(f'Password: {password} -> APR1 Hash: {hashed_password}')
