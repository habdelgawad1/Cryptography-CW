# Cryptography Milestone 2

This project contains an educational implementation of the Data Encryption
Standard (DES), together with scripts that demonstrate DES rounds, ECB mode,
and encrypted client/server communication.

> **Security notice:** DES has an effective 56-bit key and is cryptographically
> obsolete. ECB mode also reveals repeated plaintext blocks. This code is for
> coursework and experimentation only; do not use it to protect real data.

## Requirements

- Python 3.9 or later
- No third-party packages

All scripts are intended to be run from this directory.

## Files

| File | Purpose |
| --- | --- |
| `des.py` | DES tables and primitives, key scheduling, block encryption/decryption, and padded ECB helpers. It also runs a published DES self-test when executed or imported. |
| `appendix_a.py` | Prints the DES key schedule and all intermediate values from round 1 for `SEND1500` using the key `LEG-BANK`. |
| `appendix_b.py` | Encrypts a message block-by-block and shows the resulting ciphertext. It demonstrates that identical ECB plaintext blocks produce identical ciphertext blocks. |
| `server.py` | Listens on `127.0.0.1:5050`, receives length-prefixed ciphertext, decrypts it, and displays the plaintext. |
| `client.py` | Reads terminal messages, encrypts them with padded ECB, and sends them to the server. |

## Quick start

### Run the DES self-test

```text
python des.py
```

The script should print:

```text
DES self-test passed: 85E813540F0AB405
```

### Inspect the first DES round

```text
python appendix_a.py
```

### Demonstrate ECB encryption

The default message contains repeated blocks:

```text
python appendix_b.py
```

To provide a custom message, pass a string whose length is a multiple of
8 bytes:

```text
python appendix_b.py SEND$100SEND$100SEND$900
```

### Run the encrypted client and server

Open two terminals in the project directory.

In the first terminal:

```text
python server.py
```

In the second terminal:

```text
python client.py
```

Enter messages at the client prompt. Press `Ctrl+C` or send end-of-file to
disconnect. The server accepts one client at a time. For a single demonstration
session, start it with:

```text
python server.py --once
```

## Protocol

The client sends each encrypted message as:

1. A 4-byte unsigned big-endian ciphertext length.
2. The ciphertext bytes.

The server rejects empty, non-block-aligned, or oversized frames. The shared
demonstration key is `LEG-BANK`, and the default address is
`127.0.0.1:5050`.

## Python API example

```python
from des import ecb_decrypt, ecb_encrypt

key = b"LEG-BANK"
ciphertext = ecb_encrypt(b"example message", key)
plaintext = ecb_decrypt(ciphertext, key)
assert plaintext == b"example message"
```

