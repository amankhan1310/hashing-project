import pandas as pd
import hashlib
import re
import os

INPUT_FILE = "sample_input.xlsx"
OUTPUT_FILE = "output.csv"
SALT = os.getenv("HASH_SALT")

CHUNK_SIZE = 200000


def clean_mobile(value):
    digits = re.sub(r"\D", "", str(value))
    if len(digits) >= 10:
        return digits[-10:]
    return None


def generate_hash(mobile):
    if not SALT:
        raise ValueError("HASH_SALT is not set")

    formatted = "91" + mobile
    text = SALT + formatted
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    start = 0
    first_write = True

    while True:
        df = pd.read_excel(
            INPUT_FILE,
            header=None,
            skiprows=start,
            nrows=CHUNK_SIZE,
            dtype=str
        )

        if df.empty:
            break

        hashes = []

        for value in df[0]:
            m = clean_mobile(value)
            if m:
                hashes.append(generate_hash(m))

        pd.DataFrame({"sha256": hashes}).to_csv(
            OUTPUT_FILE,
            mode="a",
            index=False,
            header=first_write
        )

        first_write = False
        start += CHUNK_SIZE

        print(f"Processed {start:,} rows")

    print("Hashing complete")


if __name__ == "__main__":
    main()