class utils:

    # Code used from https://www.programiz.com/python-programming/examples/reverse-a-number
    def reversed(num: int) -> int:
        return (int(str(num)[::-1]))

    # Code used from https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
    def formatter(num: int) -> list:
        binary_str = format(num, 'b')
        octal_str = format(num, 'o')
        num_list = [int(binary_str), int(octal_str)]
        return (num_list)
