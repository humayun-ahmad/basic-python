from cryptography.fernet import Fernet

def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)


def load_key():
	return open("key.key", "rb").read()

write_key()
key = load_key()

f = Fernet(key)
message = "Some message".encode()
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)

print(str(decrypted) + " : " + str(encrypted))
