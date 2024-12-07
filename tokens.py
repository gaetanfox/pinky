class Token:
    def __init__(self, token_type, lexeme) -> None:
        self.token_type = token_type
        self.lexeme = lexeme

    def __repr__(self) -> str:
        return f"({self.token_type}, {self.lexeme})"
