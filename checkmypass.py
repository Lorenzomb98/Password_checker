# Importing necessary modules
import requests
import hashlib
import sys

# Fetching pwnedpasswords API
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}')
    return response

# Comparing user provided password hash to leaked hashes on API
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count    
    return 0
    
'''
 This program converts your password to a sha1 hash,
 fetches the hashes from the API that match the first 5 characters of the user's hash,
 and locally compares the fetched hashes to the user's complete hash, 
 always keeping the user's complete hash on the machine

 # To use the program, simply write "python checkmypass.py <password>" in the terminal
'''
def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, you should probably change your password')
        else:
            print(f'{password} was not found. Great!')
    return 'done!'

# To use the program, simply write "python checkmypass.py <password>" in the terminal
sys.exit(main(sys.argv[1:]))


