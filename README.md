# Password_checker
This program checks if your password has been leaked by using the Pwnedpasswords API. It does this by converting the password to a SHA-1 hash, fetching the hashes from the API that match the first 5 characters of the user's hash, and locally comparing the fetched hashes to the user's complete hash, always keeping the user's complete hash on the machine.
