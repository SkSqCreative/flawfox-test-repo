# Potential debug mode enabled
# Assuming Flask context
class App:
    debug = True

app = App()
if app.debug:
    print('Debug mode is ON')

# Hardcoded secret
config = {
    'SECRET_KEY': 'SuperSecretPassword12345abcde',
    'API_KEY': 'ak_live_abcdefghijklmnopqrstuvwxyz0123456789',
}
print(f"Using API Key: {config['API_KEY']}")
