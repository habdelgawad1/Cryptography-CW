"""Calculate and display the DES left and right halves after round 1."""

from des import E, IP, P, PC1, PC2, SHIFTS, bytes_to_bits
from des import permute, rotate_left, sbox_lookup, xor


KEY = b"LEG-BANK"
PLAINTEXT = b"SEND1500"


def feistel(r: list[int], subkey: list[int]) -> tuple[
    list[int], list[int], list[int], list[int]
]:
    """Return the intermediate values from one DES Feistel function."""
    expanded = permute(r, E)
    mixed = xor(expanded, subkey)
    sbox_output = []
    for box in range(8):
        value = sbox_lookup(mixed[box * 6:box * 6 + 6], box)[2]
        sbox_output.extend((value >> shift) & 1 for shift in range(3, -1, -1))
    return expanded, mixed, sbox_output, permute(sbox_output, P)


def bits_hex(bits: list[int]) -> str:
    """Convert a bit list to uppercase hexadecimal."""
    return f"{int(''.join(map(str, bits)), 2):0{len(bits) // 4}X}"


def bits_binary(bits: list[int]) -> str:
    """Convert a bit list to a binary string."""
    return "".join(map(str, bits))


def show(label: str, bits: list[int]) -> None:
    """Print a labelled binary value."""
    print(f"{label:<24} {bits_binary(bits)}")


def main() -> None:
    """Print binary values for each stage of one DES round."""
    plaintext_bits = permute(bytes_to_bits(PLAINTEXT), IP)
    left0, right0 = plaintext_bits[:32], plaintext_bits[32:]

    key_bits = permute(bytes_to_bits(KEY), PC1)
    c0, d0 = key_bits[:28], key_bits[28:]
    c1 = rotate_left(c0, SHIFTS[0])
    d1 = rotate_left(d0, SHIFTS[0])
    k1 = permute(c1 + d1, PC2)

    print("Key schedule")
    show("Key after PC-1", key_bits)
    show("C0", c0)
    show("D0", d0)
    show("C1", c1)
    show("D1", d1)
    show("K1", k1)

    print("\nInitial permutation")
    show("IP(plaintext)", plaintext_bits)
    show("L0", left0)
    show("R0", right0)

    expanded, mixed, sbox_output, permutation = feistel(right0, k1)
    left1 = right0
    right1 = xor(left0, permutation)

    print("\nRound 1 Feistel function")
    show("E(R0)", expanded)
    show("E(R0) XOR K1", mixed)
    show("S-box output", sbox_output)
    show("P(S-box output)", permutation)
    print("\nRound 1 result")
    show("L1 = R0", left1)
    show("R1 = L0 XOR P", right1)
    print(f"\nL1 hex = {bits_hex(left1)}")
    print(f"R1 hex = {bits_hex(right1)}")


if __name__ == "__main__":
    main()
