import hashlib
import random

# Weak hash
hasher = hashlib.sha1()
hasher.update(b'some data')
print(hasher.hexdigest())

# Insecure random
random_number = random.random()
print(f'Random float: {random_number}')

random_int = random.randint(1, 100)
print(f'Random int: {random_int}')
