# Test file for insecure deserialization with pickle
import pickle
import os

# Simulate loading data from an potentially untrusted source
some_data_source = b"cos\nsystem\n(S'echo vulnerable'\ntR."

def load_data(data):
    try:
        # Vulnerable line: Using pickle.loads
        loaded_object = pickle.loads(data)
        print("Object loaded successfully:", loaded_object)
        return loaded_object
    except Exception as e:
        print("Failed to load object:", e)
        return None

load_data(some_data_source)
