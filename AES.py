import aes
import time

class AES:
    def __init__(self):
        self.key = 0x000102030405060708090a0b0c0d0e0f # 128 bit key
        self.cryptos = list(bytearray())
        self.encryptor = aes.aes(self.key, 128)

    def encrypt_all(self, images):
        crypto = []
        for image in images:
            temp = self.encryptor.enc_once(aes.utils.bytes2int(bytes(image)))
            crypto.append(bytearray(temp))
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



