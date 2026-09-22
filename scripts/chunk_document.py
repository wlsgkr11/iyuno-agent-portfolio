from pathlib import Path

file_path = Path("data/security_sample.md")
text = file_path.read_text(encoding="utf-8")

# Split the document into chunks using blank lines
chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print(f"Total chunks: {len(chunks)}")
print("=" * 40)

for i, chunk in enumerate(chunks, start=1):
    print(f"[Chunk {i}]")
    print(chunk)
    print("-" * 40)
