import des
import time

class DES:
    def __init__(self):
        self.key = des.DesKey(b"abcdefgh")
        self.cryptos = list(bytearray())

    def encrypt_all(self, images):
        crypto = []
        for image in images:
            temp = self.key.encrypt(bytes(image), padding=True)
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