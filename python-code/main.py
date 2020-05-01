from pypresent import Present
import Padding
import sys
import timeit

def testing_80(): 
    text="FFFFFFFFFFFFFFFF"
    k="FFFFFFFFFFFFFFFFFFFF"

    key = bytes.fromhex(k)

    text = Padding.appendPadding(text,blocksize=8,mode='CMS')

    cipher = Present(key) 
    encrypted = cipher.encrypt(text.encode())
    decrypted = cipher.decrypt(encrypted)

def testing_128(): 
    text="FFFFFFFFFFFFFFFF"
    k="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

    key = bytes.fromhex(k)

    text = Padding.appendPadding(text,blocksize=8,mode='CMS')

    cipher = Present(key) 
    encrypted = cipher.encrypt(text.encode())
    decrypted = cipher.decrypt(encrypted)


for i in range(0,2):
    print("Time (ns/op) for 80-bit key. \t Round {}:".format(i), timeit.timeit("testing_80()", number=1000,  setup="from __main__ import testing_80")/1000)

for i in range(0,2):
    print("Time (ns/op) for 128-bit key. \t Round {}:".format(i), timeit.timeit("testing_128()", number=1000,  setup="from __main__ import testing_128")/1000)
