from Application.CalculatorMain import CalculatorSolver
from UI.Interface import Display


class Messenger:
    def __init__(self, display: Display):
        self.display = display
        self.display_val = []
        self.answer_displayed = False
        self.calculator_engine = CalculatorSolver()

    def button_pressed(self, number: int):
        if number > -1:  # Number
            if self.answer_displayed:
                self.display_val.clear()
                self.answer_displayed = False

            self.display_val.append(str(number))
            self.display.update_display(''.join(self.display_val))

        elif number == -1:  # Clear
            self.clear()
            self.display.update_display(0.0)
            self.answer_displayed = False
        elif number == -2:  # Division
            is_valid = self.check_input('/')
            if is_valid:
                self.display_val.append('/')
                self.display.update_display(''.join(self.display_val))
                self.answer_displayed = False
        elif number == -3:  # Multiplication
            is_valid = self.check_input('*')
            if is_valid:
                self.display_val.append('*')
                self.display.update_display(''.join(self.display_val))
                self.answer_displayed = False
        elif number == -4:  # Subtraction
            if ''.join(self.display_val) == 'ERROR DIVISION BY ZERO':
                self.display_val.clear()
            is_valid = self.check_input('-')
            if is_valid:
                self.display_val.append('-')
                self.display.update_display(''.join(self.display_val))
                self.answer_displayed = False
        elif number == -5:  # Addition
            is_valid = self.check_input('+')
            if is_valid:
                self.display_val.append('+')
                self.display.update_display(''.join(self.display_val))
                self.answer_displayed = False
        elif number == -6:  # Equal
            if self.answer_displayed:
                return
            try:
                result = self.calculator_engine.solve_expression(''.join(self.display_val))
                result = 0.0 if result is None else result
                self.calculator_engine.clean()
                self.display.update_display(result)
                self.clear()
                for char in str(result):
                    self.display_val.append(str(char))
                self.answer_displayed = True
            except ValueError:
                self.calculator_engine.clean()
                self.answer_displayed = False
            except IndexError:
                self.calculator_engine.clean()
                self.answer_displayed = False
        elif number == -7:  # Dot
            if self.answer_displayed:
                self.display_val.clear()

            is_valid = self.check_input('.')
            if is_valid:
                self.display_val.append('.')
                self.display.update_display(''.join(self.display_val))
                self.answer_displayed = False

    # returns true if it is valid input, false if invalid input
    # Inputs: digits(0-9), '+', '-', '/', '*', '.'
    def check_input(self, char):
        # first input check
        if not self.display_val:
            if char is '+' or char is '/' or char is '*':
                return False
            else:
                return True

        if self.display_val[0] is '-' and len(self.display_val) == 1:
            if char is not '.':
                return False

        previous = self.display_val[-1]
        try:
            previous_2 = self.display_val[-2]
        except IndexError:
            previous_2 = None

        # + / * can't come after symbols
        if not str.isdigit(previous):
            if char is '+' or char is '/' or char is '*':
                return False
            elif previous is '.':  # only digits come after dot
                if not str.isdigit(char):
                    return False

        # - sign what comes after check. three negative signs in a row invalid
        if previous is '-' and previous_2 is '-':
            if char is '-':
                return False

        return True

    def clear(self):
        self.display_val = []
