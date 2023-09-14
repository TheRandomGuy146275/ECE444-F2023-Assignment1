class utils:
    def reversed(num: int) -> int:
        return (int(str(num)[::-1]))

    def formatter(num: int) -> list:
        binary_str = format(num, 'b')
        octal_str = format(num, 'o')
        num_list = [int(binary_str), int(octal_str)]
        return (num_list)
