import pandas as pd
import hashlib
import re
from pathlib import Path

INPUT_FILE = Path("sample_input.csv")
OUTPUT_FILE = Path("output_new_hashed.csv")
CHUNK_SIZE = 200_000


def generate_hash(data):
    if pd.isna(data):
        return None

    value = str(data).strip()
    digits = re.sub(r"\D", "", value)

    if digits:
        return hashlib.md5(digits.encode("utf-8")).hexdigest()

    return None


def main():
    first_write = True

    for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE, dtype=str):
        mobiles = chunk["mobile"]

        hashes = [generate_hash(m) for m in mobiles]

        result = pd.DataFrame({
            "md5_hash": hashes
        })

        result.to_csv(
            OUTPUT_FILE,
            mode="a",
            index=False,
            header=first_write
        )

        first_write = False
        print("Processed one chunk...")

    print("File processed successfully.")


if __name__ == "__main__":
    main()