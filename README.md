Caesar Cipher Implementation

Description

This Python program allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

Features :
1. Encrypt a message using a specified shift value.

2. Decrypt a message using the same shift value.

3. Handle both uppercase and lowercase letters.

4. Ignore non-alphabetic characters while preserving them in the output.

Requirements : 

Python 3.x

Usage

Clone or download the repository 

Run the script using Python:

python caesar_cipher.py

Enter the message and shift value as prompted.

Choose to encrypt or decrypt the message.

Example

Encryption:

Enter message: hello world
Enter shift value: 3
Encrypted message: khoor zruog

Decryption:

Enter message: khoor zruog
Enter shift value: 3
Decrypted message: hello world

Algorithm

Take user input for the message and shift value.

Iterate through each character in the message.

If the character is a letter:

Shift it forward (for encryption) or backward (for decryption) based on the shift value.

Maintain case sensitivity.

Preserve spaces and non-alphabetic characters.

Display the transformed text.

License

This project is open-source and available under the MIT License.

Contributions

Feel free to contribute by improving the program, fixing bugs, or adding new features. Fork the repository and submit a pull request.

Contact

For any questions or suggestions, feel free to reach out!
