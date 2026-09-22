POLICIES = {
    "password": {
        "title": "Password Security Policy",
        "description": "Passwords should be stored using secure password hashing methods such as Argon2id, bcrypt, or scrypt.",
        "source": "OWASP Password Storage Cheat Sheet"
    },
    "authentication": {
        "title": "Authentication Policy",
        "description": "Applications should use strong authentication mechanisms and protect authentication credentials.",
        "source": "OWASP Authentication Cheat Sheet"
    },
    "session": {
        "title": "Session Management Policy",
        "description": "Session identifiers should be protected and securely managed throughout the user session.",
        "source": "OWASP Session Management Cheat Sheet"
    },
    "logging": {
        "title": "Logging Policy",
        "description": "Security-relevant events should be logged while sensitive information should not be unnecessarily exposed in logs.",
        "source": "OWASP Logging Cheat Sheet"
    }
}


def policy_lookup(topic):
    """
    간단한 보안 정책 조회 Tool
    """

    topic = topic.lower()

    for key, policy in POLICIES.items():
        if key in topic:
            return {
                "title": policy["title"],
                "description": policy["description"],
                "source": policy["source"]
            }

    return {
        "title": "Policy Not Found",
        "description": "해당 주제에 대한 정책을 찾을 수 없습니다.",
        "source": "Internal Policy Database"
    }


if __name__ == "__main__":
    print("Policy Lookup Tool Test")
    print("=" * 40)

    result = policy_lookup("password")

    print("Title:", result["title"])
    print("Description:", result["description"])
    print("Source:", result["source"])