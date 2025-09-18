
from modules.sample_dna import generate_sample_dna
from Bio.Seq import Seq

def analyze_dna(sequence: str) -> dict:
    """
    Analyze a DNA sequence and return key biological properties.
    """
    seq = Seq(sequence.upper())

    analysis = {
        "Sequence": str(seq),
        "Length": len(seq),
        "GC Content (%)": round(
            100 * (seq.count("G") + seq.count("C")) / len(seq), 2
        ) if len(seq) > 0 else 0,
        "RNA Transcription": str(seq.transcribe()),
        "Protein Translation": str(seq.translate(to_stop=True)),
        "Motif ATG Count": seq.count("ATG"),
    }

    return analysis


if __name__ == "__main__":
    print("=" * 50)
    print(" DNA SEQUENCE ANALYZER ")
    print("=" * 50)

    # Import a random DNA sequence from sample_dna.py
    dna_seq = generate_sample_dna(length=60)

    print(f"\nGenerated Random DNA Sequence:\n{dna_seq}\n")

    results = analyze_dna(dna_seq)

    for key, value in results.items():
        print(f"{key}: {value}")

    print("\n Analysis Complete!\n")
