from pathlib import Path

file_path = Path("data/security_sample.md")

text = file_path.read_text(encoding="utf-8")

print("Document reading successful!")
print("-" * 40)
print(text)
