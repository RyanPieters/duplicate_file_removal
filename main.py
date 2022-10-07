import hashlib


filename = input("Enter the input file name: ")
with open(filename, "rb") as f:
    r_bytes = f.read()
    readable_hash = hashlib.sha256(r_bytes).hexdigest()
    print(readable_hash)
