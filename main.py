import hashlib
import os
from pathlib import Path


# Removes every other element in a list
def remove_every_other(my_list):
    return my_list[::2]
    pass


# Required Variables
directory = Path(__file__).parent
all_hashes = []
dup_hashes = []
dup = ""
dup_files = []

# main for loop
for filename in os.listdir(directory):
    if filename.endswith(".jpg" or ".png"):
        with open(filename, "rb") as f:
            r_bytes = f.read()  # read entire file as bytes
            readable_hash = hashlib.sha256(r_bytes).hexdigest();
            all_hashes.append(readable_hash)
print("Current elements to check:", len(all_hashes))

for current_hash in all_hashes:
    dup_counter = 0
    for check_hash in all_hashes:
        if current_hash == check_hash:
            dup_counter = dup_counter + 1
    if dup_counter > 1:
        dup = current_hash
        dup_hashes.append(dup)

dup_hashes = remove_every_other(dup_hashes)

print("Current duplicate elements:", len(dup_hashes))

for dup_hash in dup_hashes:
    for filename in os.listdir(directory):
        if filename.endswith(".jpg" or ".png"):
            with open(filename, "rb") as f:
                r_bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(r_bytes).hexdigest();
                if dup_hash == readable_hash:
                    dup_files.append(filename)

for files in dup_files:
    print(dup_files)
