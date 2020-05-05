# Python PRESENT

pypresent.py contains the encryption code. timer.py includes code that times the PRESENT encryption/decryption operation. 

## Examples


```
$ python3 main.py 
usage: main-dev.py [-h] [-v] [-k KEY] [-t TEXT] [-b BENCHMARK]

Python Present

optional arguments:
  -h, --help                           show this help message and exit
  -v, --verbose
  -k KEY, --key KEY                    Key to be used
  -t TEXT, --text TEXT                 Text to encrypt
  -b BENCHMARK, --benchmark BENCHMARK  Define number of rounds.
```

Show some samples with `--verbose` output. 
```
$ python3 main.py --verbose
### PRESENT 80-bit ###
Text:	Frosty
Key:	AAAAAAAAAAAAAAAAAAAA
--------
Cipher:		7d040713c652ce56
Decrypted:	Frosty

### PRESENT 128-bit ###
Text:	Frosty
Key:	AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
--------
Cipher:		2def6690d373e23c
Decrypted:	Frosty
```

Benchmark the speed of the cipher in both 80 and 128 bit key size formats using `-b` argument. The argument takes a number to instruct the number of rounds to be performed. 

```
$ python3 main.py -b 10000
Performing 10000 rounds
Present_80	10.4032 seconds
Present_128	10.6847 seconds
```

