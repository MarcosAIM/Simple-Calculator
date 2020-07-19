class CalculatorSolver:
    def __init__(self, expression_string: str = None):
        self.expression_string = expression_string
        self.expression_list = []

    def string_to_list(self, string):
        current_number = []
        for char in string:
            if str.isdigit(char) or char is '.':
                current_number.append(char)
            else:
                if not current_number:
                    if char == '-':
                        current_number.append(char)
                else:
                    self.expression_list.append(float(''.join(current_number)))
                    current_number.clear()
                    self.expression_list.append(char)
            # last number
        if current_number:
            self.expression_list.append(float(''.join(current_number)))

    def solve_expression(self, expression_str: str = None):
        if expression_str:
            self.expression_string = expression_str

        if not self.expression_list:
            if self.expression_string:
                self.string_to_list(self.expression_string)
            else:
                return

        while len(self.expression_list) > 1:
            position = 1
            operator1 = None
            operator2 = None

            try:
                operator1 = self.expression_list[position]
                operator2 = self.expression_list[position + 2]
            except IndexError:
                pass

            if operator1 is '/' or operator1 is '*':
                error = self.solve_operation(position)
                if error:
                    self.expression_list.clear()
                    return 'ERROR DIVISION BY ZERO'
            elif operator2 is '/' or operator2 is '*':
                error = self.solve_operation(position + 2)
                if error:
                    self.expression_list.clear()
                    return 'ERROR DIVISION BY ZERO'
            else:
                self.solve_operation(position)

        result = self.expression_list[0]
        self.expression_list.clear()
        return result

    def solve_operation(self, number):
        operand1 = self.expression_list[number - 1]
        operator = self.expression_list[number]

        if operator is '+':
            self.expression_list[number] = operand1 + self.expression_list[number + 1]
        elif operator is '-':
            self.expression_list[number] = operand1 - self.expression_list[number + 1]
        elif operator is '*':
            self.expression_list[number] = operand1 * self.expression_list[number + 1]
        else:
            try:
                self.expression_list[number] = operand1 / self.expression_list[number + 1]
            except ZeroDivisionError:
                return True
        self.expression_list.pop(number - 1)
        self.expression_list.pop(number)

    def clean(self):
        self.expression_string = None
        self.expression_list = []
