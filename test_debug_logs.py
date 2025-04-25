# Test file for Python print() debug detection

import os
# import logging # Example of using proper logging

# logging.basicConfig(level=logging.INFO)

def load_config():
    api_key = os.environ.get("API_KEY", "default_key")
    print(f"API Key loaded: {api_key}") # This should be flagged
    # logging.info(f"API Key loaded (first 5 chars): {api_key[:5]}...") # Safer logging example
    return api_key

def process_data(data):
    print("Starting data processing...") # This should be flagged
    processed_value = data * 2
    if processed_value > 10:
        print(f"Processed value {processed_value} is large!") # Indented print, should be flagged
    
    # print("Processing finished.") # Commented out, should NOT be flagged
    return processed_value

config = load_config()
result = process_data(5)
print(f"Final result: {result}") # This should be flagged
