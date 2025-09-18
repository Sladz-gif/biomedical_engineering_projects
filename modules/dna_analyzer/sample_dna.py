# modules/dna_analyzer.py
from Bio.Seq import Seq
from modules.sample_dna import generate_sample_dna

def analyze_dna_sequence(sequence: str):
    """
    Analyzes a DNA sequence and returns useful biological properties.
    """
    seq = Seq(sequence.upper())

    results = {
        "Original Sequence": str(seq),
        "Length": len(seq),
        "GC Content (%)": round(
            100 * float(seq.count("G") + seq.count("C")) / len(seq), 2
        ) if len(seq) > 0 else 0,
        "Transcription (DNA -> RNA)": str(seq.transcribe()),
        "Translation (DNA -> Protein)": str(seq.translate(to_stop=True)),
        "Motif 'ATG' Count": seq.count("ATG"),
    }

    return results


if __name__ == "__main__":
    print("=" * 50)
    print("DNA SEQUENCE ANALYZER")
    print("=" * 50)

    # Step 1: Generate random DNA
    dna_seq = generate_sample_dna()

    # Step 2: Analyze it
    print(f"\n🧬 Analyzing random sequence: {dna_seq}\n")
    results = analyze_dna_sequence(dna_seq)

    for key, value in results.items():
        print(f"{key}: {value}")

    print("\n✨ DNA Analysis Complete!")
