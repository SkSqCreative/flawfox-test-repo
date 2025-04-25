# Test file for weak MD5 hash detection

import hashlib

def create_bad_hash(password):
    # This should trigger the MD5 warning
    hashed_pw = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hashed_pw

def create_good_hash(password):
    # This uses a stronger hash
    hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pw

# Variable name might also be relevant contextually, though the pattern focuses on usage
md5_variable = "some value"

password = "mysecretpassword"
weak_hash = create_bad_hash(password)
strong_hash = create_good_hash(password)

# Using print here will also be flagged by the debug pattern
print(f"Weak MD5 hash: {weak_hash}")
print(f"Strong SHA256 hash: {strong_hash}")
