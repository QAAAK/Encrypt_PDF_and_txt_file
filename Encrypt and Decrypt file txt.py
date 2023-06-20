import pyAesCrypt

password = input('Enter the password: ')

# Encrypt file
pyAesCrypt.encryptFile('file.txt','file_encrypt.txt', password)

# Decrypt file
pyAesCrypt.decryptFile('file_aes.txt', 'file_decrypt', password)