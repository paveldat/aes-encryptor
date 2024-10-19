## AES Encryptor/Decryptor
### Description
This project provides a class AESEncryptor for encrypting and decrypting text using the AES (Advanced Encryption Standard) algorithm. The class includes methods for both encryption and decryption, ensuring secure data transmission.


### Installation
To use this project, you need to install the required dependencies. You can do this using poetry:
```sh
pip install pdat-aes-encryptor
```

or 

```sh
poetry add pdat-aes-encryptor
```

### Usage
#### Encryption
To encrypt text, use the encrypt_aes method:
```python
from aes_encryptor import AESEncryptor

key = "your_secret_key_here"  # Ensure the key length is 16, 24, or 32 characters
plain_text = "Hello, World!"
encrypted_text = AESEncryptor.encrypt_aes(plain_text, key)
print(f"Encrypted text: {encrypted_text}")

```

#### Decryption
To decrypt text, use the decrypt_aes method:
```python
from aes_encryptor import AESEncryptor

key = "your_secret_key_here"  # Ensure the key length is 16, 24, or 32 characters
cipher_text = b'\xbb\x08\x80\xc3\r\\V\xa8D\x1f\x82$\xf6\xca8\xe0 \xa1>\x8c\x9fj+{\xb5\xcf\xf7\xa8\xf7\x85O\xf4'
decrypted_text = AESEncryptor.decrypt_aes(cipher_text, key)
print(f"Decrypted text: {decrypted_text}")
```
