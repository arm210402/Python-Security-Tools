# Network Scanner (wifi_devices_connected.py)
This script allows you to scan your local network to detect devices connected to it. It uses the Scapy library to craft and send ARP packets to broadcast addresses and get responses from devices on the network.

## Usage
1. Replace the 'xxx.xxx.xx.x' with the IP address of your network in the script.
2. Run the script.
3. The output will be a list of dictionaries containing the IP and MAC addresses of devices connected to your network.

<br>
<br>

# File Encryption/Decryption (encdy.py)
This script allows you to encrypt and decrypt files using the Advanced Encryption Standard (AES) algorithm. It uses the PyCrypto library to perform the encryption and decryption.

## Usage
1. Replace 'your_key_here' in the main function with your own secret key.
2. Call the encrypt_file function with the name of the file you want to encrypt as an argument.
3. Call the decrypt_file function with the name of the encrypted file as an argument.
4. The output will be a decrypted file with the same name as the original file.

<br>
<br>

# Password Guessing (dictatt.py)
This script allows you to guess the password of a target user account on a website. It uses the Requests library to make POST requests to the login page with different passwords until it finds the correct one.

## Usage
1. Replace the 'url', 'passwords', and 'username' variables with the appropriate values for your target website and account.
2. Run the script.
3. If the correct password is found, it will be printed to the console.
