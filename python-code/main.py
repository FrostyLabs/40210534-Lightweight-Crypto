from pypresent import Present
import argparse
import Padding
import sys
from timer import Timer


def parse_options():
    """
    Parse the arguments
    """

    global parser
    formatter = lambda prog: argparse.HelpFormatter(prog,max_help_position=50)
    parser = argparse.ArgumentParser(description="Python Present", formatter_class=formatter)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-k", "--key", type=str, help="Key to be used", required=False)
    parser.add_argument("-t", "--text", type=str, help="Text to encrypt", required=False)
    parser.add_argument("-b", "--benchmark", type=int, help="Define number of rounds. ", required=False)

    args = parser.parse_args()
    return args

def present_80(text, k): 
    """
    Present cipher with 80-bit key
    """

    key = bytes.fromhex(k)
    text = Padding.appendPadding(text,blocksize=8,mode='CMS')

    cipher = Present(key) 
    encrypted = cipher.encrypt(text.encode())
    decrypted = cipher.decrypt(encrypted)

    if args.verbose: 
        print ("### PRESENT 80-bit ###")
        print ("Text:\t{}".format(text))
        print ("Key:\t{}".format(k))
        print ("--------")
        print ("Cipher:\t\t"+encrypted.hex())
        print ("Decrypted:\t{}\n".format(Padding.removePadding(decrypted.decode(),blocksize=8,mode='CMS')))

def present_128(text, k):
    """
    Present cipher with 128-bit key
    """

    key = bytes.fromhex(k)
    text = Padding.appendPadding(text,blocksize=8,mode='CMS')

    cipher = Present(key)
    encrypted = cipher.encrypt(text.encode())
    decrypted = cipher.decrypt(encrypted)

    if args.verbose: 
        print ("### PRESENT 128-bit ###")
        print ("Text:\t{}".format(text))
        print ("Key:\t{}".format(k))
        print ("--------")
        print ("Cipher:\t\t"+encrypted.hex())
        print ("Decrypted:\t{}".format(Padding.removePadding(decrypted.decode(),blocksize=8,mode='CMS')))

def benchmark(): 
    """
    Benchmark PRESENT cipher with 80 bit and
    128 bit keys. Time the duration and report
    """

    if not args.verbose: 
        plain = "AAAAAAAA"
        key_80 = "AAAAAAAAAAAAAAAAAAAA"
        key_128 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        p_80 = Timer()
        p_80.start()
        
        for _ in range(0,args.benchmark):
            present_80(plain, key_80)
       
        print(f"Present_80\t{p_80.stop():0.4f} seconds")

        p_128 = Timer()
        p_128.start()
        
        for _ in range(0,args.benchmark):
            present_128(plain, key_128)
       
        print(f"Present_128\t{p_128.stop():0.4f} seconds")
    
def main(args):
    if len(sys.argv) == 1: 
        parser.print_help()
        sys.exit(0)

    if isinstance(args.benchmark, int):
        print("Performing {} rounds".format(args.benchmark))
        benchmark()

    plaintext = "hello"
    cryptKey_80 = "AAAAAAAAAAAAAAAAAAAA"
    cryptKey_128 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    if (args.text): 
        plaintext = args.text

    if (args.key):
        if (len(args.key) == 20): 
            cryptKey_80 = args.key
        if (len(args.key) == 32): 
            cryptKey_128 = args.key

    if args.verbose: 
        present_80(plaintext, cryptKey_80)
        present_128(plaintext, cryptKey_128)
    
if __name__ == "__main__":
    args = parse_options()
    main(args)
