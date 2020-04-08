# Current status
  - The code is able to run with 8 byte plaintext, and 10 or 16 byte key
  - The code times the duration of the cipher encryption and decryption

## Todo
  - [ ] Implement the testing functions

Generate the binary:
```
$ go build -o outfile
```


Testing the binary:
```
$ ./outfile
[!] Please make sure:
 - To only use 2 arguments
 - That that plaintext is 8 bytes
 - That the key is 10 or 16 bytes
	Usage: ./outfile Plaintext Key

[+] Here is a sample.
[+] Plaintext and key both set as a null bytearray

	Plaintext  : 0000000000000000
	Key        : 00000000000000000000
	Ciphertext : 5579c1387b228445
	Decipher   : 0000000000000000
2020/04/08 19:45:47 ciphering took 404ms
```
Running the binary with 8 byte plaintext and 10 byte key:
```
$ ./outfile AAAAAAAA AAAAAAAAAA
	Plaintext  : 4141414141414141
	Key        : 41414141414141414141
	Ciphertext : 902545ba28d3193f
	Decipher   : 4141414141414141
2020/04/08 19:50:56 ciphering took 461ms
```


Note: I used the present repo suggested in the [GoDoc](https://godoc.org/github.com/yi-jiayu/PRESENT.go). The GitHub repository is [here](https://github.com/yi-jiayu/PRESENT.go), used at commit `3a4450fb5c2634b2fdc1443c3d0eef0538a529b1`
