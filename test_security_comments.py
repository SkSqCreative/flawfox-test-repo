import os

def process_user_input(data):
    # TODO: Security - Need to sanitize the input 'data' before using it.
    print(f"Processing: {data}")
    # FIXME: Validate the length here to prevent overflow?
    pass

raw_input = "<script>alert('XSS')</script>"
process_user_input(raw_input)

# XXX Security: This path logic is probably unsafe, review later
file_path = os.path.join('/tmp', raw_input)

# Another comment style
# TODO : security check required
def another_function():
    # fixme: encode output
    print("Another function executed.")
