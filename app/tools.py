def calculator(expression):
    """
    간단한 수식을 계산하는 Tool
    """

    try:
        allowed_chars = "0123456789+-*/(). "

        if not all(
            char in allowed_chars
            for char in expression
        ):
            return "허용되지 않은 문자가 포함되어 있습니다."

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return result

    except Exception as e:
        return f"계산 오류: {e}"


if __name__ == "__main__":
    print("Calculator Tool Test")
    print("=" * 40)

    expression = "120 * 0.15"

    result = calculator(expression)

    print("Expression:", expression)
    print("Result:", result)