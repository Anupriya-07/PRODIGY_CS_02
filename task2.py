from PIL import Image
import numpy as np
import sys

def main():
    print("1. Encryption\n2. Decryption")
    n=int(input("Enter your choice:"))
    if n==1:
        enc()
    elif n==2:
        dec()
    else:
        sys.exit("Invalid choice")

def enc():
    with Image.open("image.jpg") as image:
        pixels=np.array(image)
        key=np.random.randint(0,256, pixels.shape, dtype=np.uint8)
        np.save("key.npy",key)
        encpix=(pixels^key)
        encimg=Image.fromarray(encpix.astype(np.uint8))
        encimg.save("Encrypted.png")

def dec():
    with Image.open("Encrypted.png") as image:
        pixels=np.array(image)
        key=np.load("key.npy")
        decpix=(pixels^key)
        decimg=Image.fromarray(decpix.astype(np.uint8))
        decimg.save("Decrypted.png")
   
main()
