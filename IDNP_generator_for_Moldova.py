
"""
IDNP Generator and Validator for Moldova

This script can generate random valid Moldova IDNP numbers
and validate existing ones using the official checksum algorithm.
"""

import random
import argparse

def calculate_checksum(idnp12: str) -> int:
    """
    Calculate the checksum digit for the first 12 digits of an IDNP.
    Weights repeat in pattern [7, 3, 1].
    """
    if len(idnp12) != 12 or not idnp12.isdigit():
        raise ValueError("Input must be a string of 12 digits.")
    weights = [7, 3, 1] * 4
    total = sum(int(d) * w for d, w in zip(idnp12, weights))
    return total % 10

def generate_idnp() -> str:
    """
    Generate a random valid 13-digit IDNP.
    """
    idnp12 = ''.join(str(random.randint(0, 9)) for _ in range(12))
    checksum = calculate_checksum(idnp12)
    return idnp12 + str(checksum)

def validate_idnp(idnp: str) -> bool:
    """
    Validate a 13-digit IDNP using the checksum.
    """
    if len(idnp) != 13 or not idnp.isdigit():
        return False
    return calculate_checksum(idnp[:-1]) == int(idnp[-1])

def main():
    parser = argparse.ArgumentParser(description="Moldova IDNP Generator and Validator")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of IDNPs to generate")
    parser.add_argument("-v", "--validate", type=str, help="Validate the given IDNP")
    args = parser.parse_args()

    if args.validate:
        valid = validate_idnp(args.validate)
        status = "VALID" if valid else "INVALID"
        print(f"IDNP {args.validate} is {status}.")
    else:
        for _ in range(args.number):
            print(generate_idnp())

if __name__ == "__main__":
    for i in range (5):
        main()
