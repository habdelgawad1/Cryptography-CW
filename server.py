import socket
import struct
import sys

from des import BLOCK, ecb_decrypt


HOST, PORT = "127.0.0.1", 5050
KEY = bytes.fromhex("133457799BBCDFF1")
MAX_MESSAGE_SIZE = 65536


def receive_exact(connection: socket.socket, size: int) -> bytes:
    """Read exactly `size` bytes because recv() may return partial data."""
    data = b""
    while len(data) < size:
        part = connection.recv(size - len(data))
        if not part:
            raise ConnectionError("peer closed connection")
        data += part
    return data


def handle_client(connection: socket.socket, address) -> None:
    """Receive, decrypt, and display all messages from one client."""
    print(f"[server] connection from {address[0]}:{address[1]}")

    try:
        while True:
            # Read the 4-byte big-endian length added by the client.
            try:
                length = struct.unpack(">I", receive_exact(connection, 4))[0]
            except ConnectionError:
                break

            # Reject invalid or oversized frames before allocating/reading them.
            if length == 0 or length > MAX_MESSAGE_SIZE or length % BLOCK:
                print(f"[server] rejected frame of length {length}")
                break

            # Read the complete ciphertext, then decrypt and remove its padding.
            ciphertext = receive_exact(connection, length)
            print(f"[server] received ciphertext ({length} bytes): "
                  f"{ciphertext.hex().upper()}")
            try:
                message = ecb_decrypt(ciphertext, KEY)
            except ValueError as error:
                print(f"[server] decryption failed: {error}")
                continue

            # Decode the plaintext for display; replacement keeps bad text
            # bytes from crashing the server output.
            print(f"[server] decrypted transaction : "
                  f"{message.decode('utf-8', 'replace')}")
    finally:
        # Always release the client socket when the session ends.
        connection.close()
        print("[server] connection closed")


def main() -> None:
    # --once is useful for demonstrations and automated tests.
    run_once = "--once" in sys.argv
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Allow quick restart after the previous server process exits.
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[server] listening on {HOST}:{PORT}")

        while True:
            # Accept one client and process its messages until it disconnects.
            connection, address = server.accept()
            handle_client(connection, address)
            if run_once:
                break


if __name__ == "__main__":
    main()
