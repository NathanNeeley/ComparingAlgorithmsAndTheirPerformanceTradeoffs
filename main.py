import warnings
import os
from RSA import RSA
from DES import DES
from DES3 import DES3
from AES import AES

warnings.filterwarnings('ignore')

small_dataset = list(bytearray())
large_dataset = list(bytearray())

def read_small_dataset():
    for image in os.listdir('flowers'):
        with open(os.path.join('flowers', image), 'rb') as i:
            f = i.read()
            b = bytearray(f)
            small_dataset.append(b)

def read_large_dataset():
    for subfolders in os.listdir('dogs'):
        for image in os.listdir(os.path.join('dogs', subfolders)):
            with open(os.path.join('dogs', subfolders, image), 'rb') as i:
                f = i.read()
                b = bytearray(f)
                large_dataset.append(b)

if __name__ == "__main__":
    read_small_dataset()
    read_large_dataset()
    print("RSA Encryption")
    rsa = RSA(512)
    rsa.complete(small_dataset)
    rsa.complete(large_dataset)
    print("DES Encryption")
    des = DES()
    des.complete(small_dataset)
    des.complete(large_dataset)
    print("3DES Encryption")
    des3 = DES3()
    des3.complete(small_dataset)
    des3.complete(large_dataset)
    print("AES Encryption")
    aes = AES()
    aes.complete(small_dataset)
    aes.complete(large_dataset)

