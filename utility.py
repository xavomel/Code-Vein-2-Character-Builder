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


def save_json(filepath, filedata):
    with open(filepath, mode="w") as _data:
        json.dump(filedata, _data, indent=4)


def open_file(filepath):
    with open(filepath, "r") as _file:
        return _file.read()


def save_file(filepath, filedata):
    with open(filepath, "w") as _file:
        _file.write(filedata)


# not needed?
def int_to_hexstring(number, desired_length):
    hexstring = str(hex(number)).replace("0x", "").zfill(desired_length)
    if len(hexstring) != desired_length:
        raise ValueError("number too large for desired length")
    return hexstring


# not needed?
def hexstring_to_int(hexstring):
    return int(hexstring, 16)
