import csv
from encryption import encrypt_value


def process_csv(
    input_path: str,
    output_path: str,
    key: bytes,
    columns_to_encrypt: list,
    chunk_size: int = 10000
):
    with open(input_path, newline="", encoding="latin1") as infile, \
         open(output_path, "w", newline="", encoding="latin1") as outfile:

        reader = csv.reader(infile, delimiter="|")
        writer = csv.writer(outfile, delimiter="|")

        header = next(reader)
        writer.writerow(header)

        indexes = [header.index(col) for col in columns_to_encrypt]

        batch = []
        for row in reader:
            batch.append(row)

            if len(batch) >= chunk_size:
                _process_batch(batch, indexes, key)
                writer.writerows(batch)
                batch = []

        if batch:
            _process_batch(batch, indexes, key)
            writer.writerows(batch)


def _process_batch(rows, indexes, key):
    for row in rows:
        for idx in indexes:
            row[idx] = encrypt_value(row[idx], key)
