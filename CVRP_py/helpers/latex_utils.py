def format_long_number(number):
    n = str(number)
    sp = n.split(".")
    s = sp[0]
    value = ""
    end = len(s)
    for c in range(len(s) - 3, 0, -3):
        value = r"\," + s[c:end] + value
        end = c
    value = s[:end] + value
    value = value + "." + sp[1]
    return value


def new_table_row():
    line = r" \\" + "\n" + r"\hline" + "\n"
    return line
