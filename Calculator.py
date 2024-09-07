class Calculator:
    def __init__(self) -> None:
        self.left_operand: str = "0"
        self.right_operand: str | None = None
        self.operator: str | None = None
        self.left_operand_is_decimal: bool = False
        self.right_operand_is_decimal: bool = False
        self.CANNOT_DIVIDE_BY_ZERO_ERROR_MESSAGE: str = "Cannot divide by zero"

    def handle_divide_by_zero(self, value: str) -> str:
        if value == self.CANNOT_DIVIDE_BY_ZERO_ERROR_MESSAGE:
            return "0"
        return value

    def plus(self) -> str:
        pass
    
    def minus(self) -> str:
        pass
    
    def divide(self) -> str:
        pass
    
    def multiply(self) -> str:
        pass

    def percent(self):
        if self.operator:
            left_operand = float(self.left_operand)
            if self.operator in ["-", "+"]:
                if self.right_operand:
                    right_operand = float(self.right_operand)
                else:
                    right_operand = left_operand
                self.right_operand = right_operand * left_operand / 100
            elif self.operator in ["/", "*"]:
                self.right_operand = left_operand / 100
            if int(self.right_operand) == float(self.right_operand):
                self.right_operand = str(int(self.right_operand))
                self.right_operand_is_decimal = False
            else:
                self.right_operand = str(self.right_operand)
                self.right_operand_is_decimal = True
            return self.right_operand

        self.left_operand = "0"
        return self.left_operand

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
        if self.operator:
            if self.right_operand:
                right_operand = self.right_operand[1:] if self.right_operand[0] == "0" else self.right_operand
                self.right_operand = right_operand + number
            else:
                self.right_operand = number
            return self.right_operand
        left_operand = self.left_operand[1:] if self.left_operand[0] == "0" else self.left_operand
        self.left_operand = left_operand + number
        return self.left_operand

    def clear(self) -> str:
        self.left_operand = "0"
        self.right_operand = None
        self.operator = None
        self.left_operand_is_decimal = False
        self.right_operand_is_decimal = False
        return self.left_operand