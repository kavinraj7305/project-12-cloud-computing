from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Create encryption object
cipher = Fernet(key)

# Original data
data = "Hello, this is confidential data."

print("Original Data:")
print(data)

# Encrypt the data
encrypted_data = cipher.encrypt(data.encode())

print("\nEncrypted Data:")
print(encrypted_data.decode())

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

print("\nDecrypted Data:")
print(decrypted_data.decode())