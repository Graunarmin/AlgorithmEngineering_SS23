import json


def write_json(data, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def write_txt(data, filepath):
    with open(filepath, 'w') as outfile:
        outfile.write(data)

