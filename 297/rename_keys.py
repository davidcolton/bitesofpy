from typing import Dict, Any


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:

    if isinstance(data, dict):
        new = dict()
        for key, value in data.items():
            try:
                new_key = key.replace("@", "")
            except:
                new_key = key
            new[new_key] = rename_keys(value)
    elif isinstance(data, (list)):
        new = list(rename_keys(v) for v in data)
    else:
        return data
    return new
