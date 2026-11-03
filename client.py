"""Encrypt and send transactions to the DES server from the terminal."""

import socket
import struct

from des import BLOCK, ecb_encrypt


HOST, PORT = "127.0.0.1", 5050
KEY = bytes.fromhex("133457799BBCDFF1")


def main() -> None:
    # Open one TCP connection so several messages can be sent in one session.
    with socket.create_connection((HOST, PORT)) as connection:
        print("[client] connected; enter a message, or press Ctrl+C/Ctrl+D to exit")
        try:
            while True:
                message = input("[client] message> ")
                if not message:
                    continue

                # Convert terminal text to bytes, then encrypt it with DES.
                ciphertext = ecb_encrypt(message.encode(), KEY)
                print(f"[client] plaintext  : {message}")
                print(
                    f"[client] ciphertext : {ciphertext.hex().upper()} "
                    f"({len(ciphertext)} bytes, {len(ciphertext) // BLOCK} blocks)"
                )

                # Prefix each ciphertext with a 4-byte length so the server
                # knows exactly how many bytes belong to this message.
                header = struct.pack(">I", len(ciphertext))
                connection.sendall(header + ciphertext)
        except (EOFError, KeyboardInterrupt):
            print("\n[client] disconnected")


if __name__ == "__main__":
    main()
