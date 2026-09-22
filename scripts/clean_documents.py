from pathlib import Path
from bs4 import BeautifulSoup

DATA_DIR = Path("data/public")

print("[1] Starting document cleaning...")

files = list(DATA_DIR.glob("*.md"))

print(f"[2] Documents found: {len(files)}")

for file_path in files:
    print()
    print(f"Cleaning: {file_path.name}")

    html = file_path.read_text(
        encoding="utf-8"
    )

    soup = BeautifulSoup(html, "html.parser")

    # 불필요한 HTML 영역 제거
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    # 실제 텍스트 추출
    text = soup.get_text(
        separator="\n",
        strip=True
    )

    # 빈 줄 정리
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    clean_text = "\n\n".join(lines)

    file_path.write_text(
        clean_text,
        encoding="utf-8"
    )

    print(f"Saved: {file_path.name}")

print()
print("=" * 60)
print("Document cleaning completed!")
print("=" * 60)