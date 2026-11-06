import sys

from des import BLOCK, encrypt_block


KEY = b"LEG-BANK"
DEFAULT_MESSAGE = b"SEND$100SEND$100SEND$900"


def show(message: bytes) -> None:
    if len(message) == 0 or len(message) % BLOCK:
        raise ValueError("message length must be a positive multiple of 8 bytes")

    # Step 1: encrypt the complete 64-bit blocks without padding.
    ciphertext = b"".join(
        encrypt_block(message[start:start + BLOCK], KEY)
        for start in range(0, len(message), BLOCK)
    )

    print(f"Key       : {KEY.hex().upper()}")
    print(
        f"Plaintext : {message.decode()} "
        f"({len(message)} bytes, {len(message) // BLOCK} blocks)\n"
    )
    print(
        f"{'Block':<6}{'Plaintext (ASCII)':<20}"
        f"{'Plaintext (hex)':<20}Ciphertext (hex)"
    )

    # Step 2: display each plaintext block and its encrypted block.
    for number, start in enumerate(range(0, len(ciphertext), BLOCK), 1):
        plaintext_block = message[start:start + BLOCK]
        ciphertext_block = ciphertext[start:start + BLOCK]
        label = plaintext_block.decode("ascii", errors="replace")
        print(
            f"{number:<6}{label:<20}{plaintext_block.hex().upper():<20}"
            f"{ciphertext_block.hex().upper()}"
        )

    # Step 3: identical plaintext blocks produce identical ECB ciphertext.
    print(
        f"\nBlock 1 == Block 2 ciphertext ? "
        f"{ciphertext[:BLOCK] == ciphertext[BLOCK:2 * BLOCK]}"
    )
    print(
        f"Block 1 == Block 3 ciphertext ? "
        f"{ciphertext[:BLOCK] == ciphertext[2 * BLOCK:3 * BLOCK]}"
    )


if __name__ == "__main__":
    show(sys.argv[1].encode() if len(sys.argv) > 1 else DEFAULT_MESSAGE)
