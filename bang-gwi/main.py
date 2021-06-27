import sys

from token import tokenize


class Flags:
    def __init__(self):
        self.variable_assigning = False


def _overflow_mask(op: int) -> int:
    return op & 0xff


class Interpreter:
    def __init__(self, stack_max_size=256, debug=False):
        self.stack_max_size = stack_max_size
        self.stack = [0 for _ in range(self.stack_max_size)]
        self.stack_pointer = 0

        self.flags = Flags()
        self._variable = 0
        self.debug = debug

    def print_memory(self):
        stack_memory = ','.join([str(i) for i in self.stack])
        print(f'stack:  {stack_memory}')
        print(f'variable: {self._variable}')
        print(f'stack pointer: {self.stack_pointer}')
        print(f'flag(variable_assigning): {self.flags.variable_assigning}')

    def run(self, code: str):
        if code == '뿡':
            assert self.flags.variable_assigning is False
            self.flags.variable_assigning = True
            self._variable = 0
        if code == '뿍뿍':
            assert self.flags.variable_assigning is True
            self._variable += 1
            self._variable = _overflow_mask(self._variable)
        if code == '뽁뽁':
            assert self.flags.variable_assigning is True
            self._variable -= 1
            self._variable = _overflow_mask(self._variable)
        if code == '~':
            assert self.flags.variable_assigning is True
            self._variable **= 2
            self._variable = _overflow_mask(self._variable)
        if code == '뿌직':
            self.stack_pointer += 1
        if code == '쀼직':
            self.stack_pointer -= 1
        if code == '북':
            # Add stack value to variable
            assert self.flags.variable_assigning is True
            self._variable += self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '부북':
            # Minus stack value to variable
            assert self.flags.variable_assigning is True
            self._variable -= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '부부북':
            # Multiple stack value to variable
            assert self.flags.variable_assigning is True
            self._variable *= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(self._variable)
        if code == '부부부북':
            # Divide stack value to variable
            assert self.flags.variable_assigning is True
            self._variable /= self.stack[self.stack_pointer]
            self._variable = _overflow_mask(int(self._variable))
        if code == '뽀옹':
            # Assign variable to stack data
            assert self.flags.variable_assigning is True
            self.stack[self.stack_pointer] = self._variable
            self.flags.variable_assigning = False
        if code == '뽀뽀옹':
            # Assign stack data to variable
            assert self.flags.variable_assigning is False
            self._variable = self.stack[self.stack_pointer]
            self.flags.variable_assigning = True
        if code == '=3':
            # Assign stack pointer to variable
            assert self.flags.variable_assigning is False
            self._variable = self.stack_pointer
            self.flags.variable_assigning = True
        if code == '==3':
            # Assign variable to stack pointer
            assert self.flags.variable_assigning is True
            self.stack_pointer = min(self._variable, self.stack_max_size)
            self.flags.variable_assigning = False
        if code == '빵':
            # Change variable to str type and assign it to stack
            string_value = str(self._variable)
            for value in reversed(string_value):
                self.stack[self.stack_pointer] = int(value)
                self.stack_pointer += 1
        if code == '빠아앙':
            # Print current stack while null access
            printing_buffer_pointer = self.stack_pointer - 1
            while printing_buffer_pointer >= 0:
                element = self.stack[printing_buffer_pointer]
                if element == 0:
                    break
                sys.stdout.write(chr(element))
                printing_buffer_pointer -= 1

        if self.debug:
            print(code)
            self.print_memory()


def main(input_file: str, debug: bool = False):
    with open(input_file, 'r') as bang_gwi_file:
        code = bang_gwi_file.read()
        thread = Interpreter(20, debug)
        for op in tokenize(code):
            thread.run(op)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='bang-gwi runtime')
    parser.add_argument('--input', default='helloworld.bang-gwi', help='Pass input `.bang-gwi` file')
    parser.add_argument('--debug', default='False', help='Debug flag (true/false)')
    args = parser.parse_args()
    main(args.input, args.debug == 'true')
