package main

// To build: 
// $ go build present.go

import (
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/yi-jiayu/PRESENT.go"
)

func encodeHex(data []byte) string {
	dst := make([]byte, hex.EncodedLen(len(data)))
	hex.Encode(dst, data)
	return string(dst)
}

func timeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %dms", name, elapsed.Nanoseconds()/1000)
}

func present_cipher(p []byte, k []byte) {
	defer timeTrack(time.Now(), "This activity")
	plaintext := []byte(p)

	key := []byte(k)
	cipher, err := present.NewCipher(key)
	if err != nil {
		log.Fatal(err)
	}

	ciphertext := make([]byte, 8)
	cipher.Encrypt(ciphertext, plaintext)

	decipher := make([]byte, 8)
	cipher.Decrypt(decipher, ciphertext)

	fmt.Printf("\t%-10s : %s\n", "Plaintext", encodeHex(plaintext))
	fmt.Printf("\t%-10s : %s\n", "Key", encodeHex(key))
	fmt.Printf("\t%-10s : %s\n", "Ciphertext", encodeHex(ciphertext))	
	fmt.Printf("\t%-10s : %s\n", "Decipher", encodeHex(decipher))
}

func main() {
	if len(os.Args) == 3 {
		present_cipher([]byte(os.Args[1]), []byte(os.Args[2]))
	} else {

		// A message on usage
		fmt.Printf("[!] Please make sure:\n")
		fmt.Printf(" - To only use 2 arguments\n")
		fmt.Printf(" - That that plaintext is 8 bytes\n")
		fmt.Printf(" - That the key is 10 or 16 bytes\n")
		fmt.Printf("\tUsage: %s Plaintext Key \n\n", os.Args[0])
		
		// Providing proof of concept
		fmt.Printf("[+] Here is a sample.\n") 
		fmt.Printf("[+] Plaintext and key both set as a null bytearray\n\n")
		present_cipher(make([]byte, 8), make([]byte, 10))
		os.Exit(3)
	}	
}
