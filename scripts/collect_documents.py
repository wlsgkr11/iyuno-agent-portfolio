import requests
from pathlib import Path

OUTPUT_DIR = Path("data/public")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

documents = [
    {
        "name": "owasp_top10.md",
        "url": "https://owasp.org/www-project-top-ten/"
    },
    {
        "name": "owasp_api_security.md",
        "url": "https://api-security.owasp.org/editions/2023/en/0x11-t10/"
    },
    {
        "name": "owasp_llm_security.md",
        "url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/"
    },
    {
        "name": "authentication.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"
    },
    {
        "name": "password_storage.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html"
    },
    {
        "name": "cryptographic_storage.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html"
    },
    {
        "name": "key_management.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html"
    },
    {
        "name": "html5_security.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html"
    },
    {
        "name": "secure_code_review.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html"
    },
    {
        "name": "security_questions.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html"
    },
    {
        "name": "csrf_prevention.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"
    },
    {
        "name": "xss_prevention.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"
    },
    {
        "name": "sql_injection_prevention.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"
    },
    {
        "name": "input_validation.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html"
    },
    {
        "name": "logging.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html"
    },
    {
        "name": "session_management.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html"
    },
    {
        "name": "transport_layer_security.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html"
    },
    {
        "name": "secure_headers.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html"
    },
    {
        "name": "file_upload.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html"
    },
    {
        "name": "docker_security.md",
        "url": "https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html"
    }
]

for document in documents:
    print(f"Downloading: {document['name']}")

    try:
        response = requests.get(
            document["url"],
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        output_file = OUTPUT_DIR / document["name"]

        output_file.write_text(
            response.text,
            encoding="utf-8"
        )

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"ERROR: {document['name']}")
        print(e)

print()
print("=" * 60)
print("Document collection completed!")
print(f"Total documents configured: {len(documents)}")
print("=" * 60)