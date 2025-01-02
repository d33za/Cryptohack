from passlib.hash import lmhash, nthash

# List of words to hash
words = ["Napier", "Foxtrot"]

# Function to print LM and NTLM hashes
def print_hashes(word):
    lm_hash = lmhash.encrypt(word)
    nt_hash = nthash.encrypt(word)
    print(f"Word: {word}")
    print(f"LM Hash: {lm_hash}")
    print(f"NT Hash: {nt_hash}")
    print("-" * 30)

# Loop through the words and print their hashes
for word in words:
    print_hashes(word)
