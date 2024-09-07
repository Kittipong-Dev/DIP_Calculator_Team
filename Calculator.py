# don't forget cannot divide by zero
class Calculator:
    def __init__(self) -> None:
        self.left_operand: str = "0"
        self.right_operand: str | None = None
        self.operator: str | None = None
        self.left_operand_is_decimal: bool = False
        self.right_operand_is_decimal: bool = False

    def plus(self) -> str:
        pass
    
    def minus(self) -> str:
        pass
    
    def divide(self) -> str:
        pass
    
    def multiply(self) -> str:
        pass

    def percent(self) -> str:
        pass

    def negate(self) -> str:
        pass

    def decimal(self) -> str:
        pass

    def get_result(self) -> str:
        pass
    
    def add_number(self, number: str) -> str:
        pass

    def clear(self) -> str:
        pass