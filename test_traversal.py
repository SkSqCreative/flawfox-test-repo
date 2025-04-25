import os

# Potential directory traversal in string
user_input = '..\..\..\etc\passwd'
# Insecure usage (don't do this!):
# file_path = os.path.join('/var/www/data', user_input)

print(f'User provided path: {user_input}')

def process_path(path_str):
    # Simulate using the potentially unsafe path
    if '../' in path_str:
        print('Path contains traversal sequence.')
    return f'Processed: {path_str}'

process_path('../../system/config.ini')
