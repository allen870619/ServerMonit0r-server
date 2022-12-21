def get_size(byte):
    try:
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if byte < factor:
                return f"{byte:.2f}{unit}B"
            byte /= factor
        return f"{byte:.2f}PB"
    except:
        return str(byte)


def emptyNullDict(dict):
    if len(dict) == 0:
        return None
    else:
        return dict
