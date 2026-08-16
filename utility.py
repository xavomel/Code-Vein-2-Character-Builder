import json


def escape_filename(filename):
    # replace : with 2 underscores
    # replace " " with 1 underscore
    return filename.replace(":", "__").replace(" ", "_")


def unescape_filename(filename):
    # replace 2 underscores with :
    # replace underscore with " "
    return filename.replace("__", ":").replace("_", " ")


def open_json(filepath):
    with open(filepath, encoding='utf-8') as _data:
        return json.load(_data)
