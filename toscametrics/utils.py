from typing import Union


def all_keys(blueprint: Union[dict, list]) -> list:
    """
    Returns a list of all the blueprint's keys
    :param blueprint: the blueprint dictionary or list
    """

    keys = list()

    if isinstance(blueprint, list):
        for item in blueprint:
            keys.extend(all_keys(item))
    elif isinstance(blueprint, dict):
        for key, value in blueprint.items():
            keys.append(key)
            keys.extend(all_keys(value))

    return keys


def all_values(blueprint: Union[dict, list]) -> list:
    """
    Returns a list of all the blueprint's primitive values
    :param blueprint: the blueprint dictionary or list
    """

    if not isinstance(blueprint, dict) and not isinstance(blueprint, list):
        return [blueprint]

    values = list()

    if isinstance(blueprint, list):
        for item in blueprint:
            values.extend(all_values(item))
    elif isinstance(blueprint, dict):
        for _, value in blueprint.items():
            values.extend(all_values(value))

    return values


def key_value_list(d):
    """ 
    This function iterates over all the key-value pairs of a dictionary and returns a list of tuple (key, value).
    d -- a dictionary to iterate through
    """
    if not isinstance(d, dict) and not isinstance(d, list):
        return []

    key_values = []

    if isinstance(d, list):
        for entry in d:
            if isinstance(entry, dict):
                key_values.extend(key_value_list(entry))
    else:
        for k, v in d.items():
            if k is None or v is None:
                continue

            key_values.append((k, v))
            key_values.extend(key_value_list(v))

    return key_values
