import json
from helpers import latex_utils as latex


def write_json(data, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def write_latex_table(data_dict, filepath, exclude_columns):
    """
    takes a dictionary with (key : dict) pairs and puts it in shape of a LaTeX Table
    """
    number_of_columns = len(data_dict[list(data_dict.keys())[0]]) - len(exclude_columns)
    table = ""

    for entry in data_dict.keys():
        # first cell
        line = r"\cellcolor{\tableHighlightColor} " + str(entry) + "\n& "
        column_count = 0

        # add values to line
        for value in data_dict[entry].keys():
            if value in exclude_columns:
                continue

            value = latex.format_long_number(str(data_dict[entry][value]))
            line += "$" + value + "$"
            column_count += 1

            # as long as we did not reach the end of the line:
            # start a new column
            if column_count != number_of_columns:
                line += "\n& "

            # when all columns for one line are done:
            # start new line
            else:
                line += latex.new_table_row()

        table += line

    with open(filepath, 'w') as outfile:
        outfile.write(table)
