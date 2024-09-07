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
        left_operand = float(self.left_operand)
        right_operand = float(self.right_operand) if self.right_operand else left_operand
        if self.operator == "+":
            left_operand += right_operand
        elif self.operator == "-":
            left_operand -= right_operand
        elif self.operator == "*":
            left_operand *= right_operand
        elif self.operator == "/":
            if right_operand != 0:
                left_operand /= right_operand
            else:
                self.clear()
                return self.CANNOT_DIVIDE_BY_ZERO_ERROR_MASSAGE
            
        if int(left_operand) == float(left_operand):
            self.left_operand = str(int(left_operand))
            self.left_operand_is_decimal = False
        else:
            self.left_operand = str(left_operand)
            self.left_operand_is_decimal = True
        
        self.operator = None
        self.right_operand = None
        self.right_operand_is_decimal = False
        return self.left_operand
    
    def add_number(self, number: str) -> str:
        pass

    def clear(self) -> str:
        pass