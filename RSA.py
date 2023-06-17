import rsa
import time

class RSA:
    def __init__(self, key_size_bytes):
        (self.pubkey, self.privkey) = rsa.newkeys(key_size_bytes)
        self.cryptos = list(bytearray())
        self.key_size_bytes = int((key_size_bytes/8) - 11)

    def encrypt_all(self, images):
        for image in images:
            bytes_encrypted = 0
            crypto = []
            while bytes_encrypted < len(image):
                temp = rsa.encrypt(image[bytes_encrypted:(self.key_size_bytes+bytes_encrypted)], self.pubkey)
                crypto.append(temp)
                bytes_encrypted = bytes_encrypted + self.key_size_bytes
            self.cryptos.append(crypto)

    def complete(self, images):
        if len(images) < 1000:
            print(f"Small Dataset of {len(images)} Images Encryption:")
        else:
            print(f"Large Dataset of {len(images)} Images Encryption:")
        start_time = time.perf_counter()
        self.encrypt_all(images)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"The execution time is: {execution_time} seconds")



