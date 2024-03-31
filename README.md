# ServerClientSecureChat

## Description
This project implements a simple client-server secure chat application using Python sockets. It also includes functionality for generating RSA key pairs, encrypting messages, and signing and verifying messages using RSA encryption.

## Usage
To run the chat application, follow the steps below:

### Server
1. Open a terminal.
2. Navigate to the directory containing the project files.
3. Run the `server.py` script.

### Client
1. Open another terminal.
2. Navigate to the directory containing the project files.
3. Run the `client.py` script.
4. Enter the server address when prompted.
5. Enter your name.
6. Start chatting.

### RSA Key Generation
1. Run the `export_pk.py` script to generate RSA key pairs.
2. Public key will be exported to `public_key.txt`.

### Message Encryption
1. Run the `functions.py` script.
2. Enter the text to be encrypted.
3. Encrypted message will be printed.

### Message Signing and Verification
1. Use `sign.py` to sign a message with a private key.
2. Use `verify.py` to verify the signature with the corresponding public key.

## Files
The project consists of the following files:

### 1. `server.py`
This script implements the server-side logic for the chat application.

### 2. `client.py`
This script implements the client-side logic for the chat application.

### 3. `export_pk.py`
This script exports RSA public key from the private key.

### 4. `functions.py`
This script contains utility functions for converting text to binary, generating random n-bit numbers, and encrypting messages.

### 5. `sign.py`
This script contains a function for signing messages using RSA encryption.

### 6. `verify.py`
This script contains a function for verifying signatures using RSA encryption.

## Requirements
This project requires Python 3.x and the following libraries:
- `Crypto` (for encryption and signing)

Install the required libraries using:
