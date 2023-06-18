def dict_to_latex_table(data_dict, exclude_columns=None):
    """
    Takes a dictionary with (key : dict) pairs and puts it in shape of a LaTeX Table.
    Optionally excludes the Columns with names given in exclude_columns
    """
    if exclude_columns is None:
        exclude_columns = []

    number_of_columns = len(data_dict[list(data_dict.keys())[0]]) - len(exclude_columns)
    table = r"\hline"

    for entry in data_dict.keys():
        # first cell
        line = r"\cellcolor{\tableHighlightColor} " + str(entry) + "\n& "
        column_count = 0

        # add values to line
        for value in data_dict[entry].keys():
            if value in exclude_columns:
                continue

            value = format_long_number(str(data_dict[entry][value]))
            line += "$" + value + "$"
            column_count += 1

            # as long as we did not reach the end of the line:
            # start a new column
            if column_count != number_of_columns:
                line += "\n& "

            # when all columns for one line are done:
            # start new line
            else:
                line += new_table_row()

        table += line

    return table


def format_long_number(number):
    """
    Adds a "\," to every third place from the back to the string of a number
    so there are little gaps at the 1000-marks in LaTeX
    """
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
    """
    Returns the string that indicates a new row in a LaTeX Table
    """
    line = r" \\" + "\n" + r"\hline" + "\n"
    return line
