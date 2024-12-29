def parse_notation(input: str) -> list:
    if input is None:
        return None
    
    if len(input) != 4:
        return None
    
    start = f_to_c(input[:2])
    end = f_to_c(input[2:])

    if start is None or end is None:
        return None

    return [start, end]


def f_to_c(field: str) -> tuple:
    x = 'abcdefgh'.find(field[0])
    y = '87654321'.find(field[1])

    if x == -1 or y == -1:
        return None

    return ('abcdefgh'.find(field[0]), '87654321'.find(field[1]))