import csv
import io

def parse_csv_and_chunk(content: str, max_chars=300):
    reader = csv.DictReader(io.StringIO(content))
    chunks = []
    for row in reader:
        summary = f"{row['Property Address']} | Suite {row['Suite']} | {row['Size (SF)']} SF | Rent {row['Rent/SF/Year']} | Broker: {row['Associate 1']} ({row['BROKER Email ID']})"
        chunks.extend([summary[i:i+max_chars] for i in range(0, len(summary), max_chars)])
    return chunks

def chunk_text(content: str, max_chars=300):
    return [content[i:i+max_chars] for i in range(0, len(content), max_chars)]
