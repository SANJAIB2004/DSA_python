import rsa

public_key, private_key = rsa.newkeys(512)

m = input("Enter the message: ").encode()
message =m
encrypted_message = rsa.encrypt(message, public_key)
print("encrypted_message:", encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print("decrypted_message:", decrypted_message)



