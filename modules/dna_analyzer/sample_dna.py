
import random

def generate_sample_dna(length=60):
    """Generate a random DNA sequence of a given length."""
    nucleotides = ["A", "T", "G", "C"]
    return "".join(random.choice(nucleotides) for _ in range(length))

if __name__ == "__main__":
    print(f"Sample DNA Sequence: {generate_sample_dna()}")
