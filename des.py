IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Eight S-boxes replace 6 input bits with 4 output bits.
SBOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]

def bytes_to_bits(data):
    """Convert bytes to bits, keeping the most-significant bit first."""
    return [(byte >> shift) & 1 for byte in data for shift in range(7, -1, -1)]


def bits_to_bytes(bits):
    """Group a bit list into bytes using the same bit ordering."""
    return bytes(
        int("".join(map(str, bits[i:i + 8])), 2)
        for i in range(0, len(bits), 8)
    )


def permute(bits, table):
    """Reorder bits according to a DES table."""
    return [bits[position - 1] for position in table]


def xor(first, second):
    """XOR two equal-length bit lists."""
    return [a ^ b for a, b in zip(first, second)]


def rotate_left(bits, count):
    """Rotate a list of bits left for the key schedule."""
    return bits[count:] + bits[:count]


def bstr(bits, group=4):
    """Display bits in groups for the DES trace."""
    text = "".join(map(str, bits))
    return " ".join(text[i:i + group] for i in range(0, len(text), group))


# Step 1: create the 16 DES round keys.
def key_schedule(key, trace=False):
    """Return the 16 48-bit round keys (and optionally the C/D halves)."""
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes (64 bits)")

    # PC-1 removes the eight parity bits and rearranges the remaining 56 bits.
    key_bits = permute(bytes_to_bits(key), PC1)
    left, right = key_bits[:28], key_bits[28:]
    subkeys, halves = [], []

    for shift in SHIFTS:
        # Each round rotates both 28-bit halves, then PC-2 selects 48 bits.
        left = rotate_left(left, shift)
        right = rotate_left(right, shift)
        halves.append((left, right))
        subkeys.append(permute(left + right, PC2))

    return (subkeys, key_bits, halves) if trace else subkeys


# Step 2: apply expansion, XOR, S-boxes, and permutation.
def sbox_lookup(six, box):
    """Return (row, col, value) for a 6-bit input to S-box `box` (0-indexed)."""
    # The first and last input bits choose the row; the middle four choose column.
    row = (six[0] << 1) | six[5]
    col = (six[1] << 3) | (six[2] << 2) | (six[3] << 1) | six[4]
    return row, col, SBOX[box][row][col]


def feistel(r, subkey):
    # Expand 32 bits to 48, mix them with the round key, then apply the S-boxes.
    expanded = xor(permute(r, E), subkey)
    out = []
    for box in range(8):
        six_bits = expanded[box * 6:box * 6 + 6]
        value = sbox_lookup(six_bits, box)[2]
        out.extend((value >> shift) & 1 for shift in range(3, -1, -1))
    # P spreads each S-box result across the 32-bit output.
    return permute(out, P)


# Step 3: encrypt or decrypt one 8-byte block.
def crypt_block(block, subkeys):
    """Apply DES to one 8-byte block using the supplied round-key order."""
    bits = permute(bytes_to_bits(block), IP)
    left, right = bits[:32], bits[32:]

    for subkey in subkeys:
        # Feistel round: the old right half becomes the new left half.
        left, right = right, xor(left, feistel(right, subkey))

    # DES swaps the halves before applying the final permutation.
    return bits_to_bytes(permute(right + left, FP))


def encrypt_block(block, key):
    """Encrypt one 8-byte block with DES."""
    return crypt_block(block, key_schedule(key))


def decrypt_block(block, key):
    """Decrypt one 8-byte block by using the round keys in reverse."""
    return crypt_block(block, key_schedule(key)[::-1])


# Step 4: add PKCS-style padding and process a message in ECB mode.
BLOCK = 8


def pad(data):
    """Pad data so its length is a multiple of the 8-byte DES block size."""
    n = BLOCK - len(data) % BLOCK
    return data + bytes([n]) * n


def unpad(data):
    """Remove padding and reject malformed padding."""
    n = data[-1]
    if not 1 <= n <= BLOCK or data[-n:] != bytes([n]) * n:
        raise ValueError("bad padding (wrong key or corrupted data)")
    return data[:-n]


def ecb_encrypt(plaintext, key):
    """Encrypt any-length data one block at a time using ECB mode."""
    subkeys = key_schedule(key)
    padded = pad(plaintext)
    return b"".join(
        crypt_block(padded[i:i + BLOCK], subkeys)
        for i in range(0, len(padded), BLOCK)
    )


def ecb_decrypt(ciphertext, key):
    """Decrypt ECB ciphertext and remove its padding."""
    if len(ciphertext) == 0 or len(ciphertext) % BLOCK:
        raise ValueError("ciphertext length must be a positive multiple of 8")
    subkeys = key_schedule(key)[::-1]
    padded = b"".join(
        crypt_block(ciphertext[i:i + BLOCK], subkeys)
        for i in range(0, len(ciphertext), BLOCK)
    )
    return unpad(padded)


# Self-test against the classic published DES test vector.
k = bytes.fromhex("133457799BBCDFF1")
pt = bytes.fromhex("0123456789ABCDEF")
ct = encrypt_block(pt, k)
assert ct.hex().upper() == "85E813540F0AB405", ct.hex()
assert decrypt_block(ct, k) == pt
print("DES self-test passed:", ct.hex().upper())
