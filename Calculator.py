class Calculator:
    def __init__(self) -> None:
        self.left_operand: str = "0"
        self.right_operand: str | None = None
        self.operator: str | None = None
        self.left_operand_is_decimal: bool = False
        self.right_operand_is_decimal: bool = False