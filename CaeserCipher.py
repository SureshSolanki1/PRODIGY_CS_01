def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.
    """
    result = ""

    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():  # Corrected typo here
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result  # Corrected indentation issue

if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter text: ")

    try:
        shift = int(input("Enter shift value: "))  # Ensure shift is an integer
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        exit()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
    else:
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
