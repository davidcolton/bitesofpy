import socket


def flatten_list(nestedList):
    """ Converts a nested list to a flat list """
    flat_list = []
    for elem in nestedList:
        if isinstance(elem, list):
            flat_list.extend(flatten_list(elem))
        else:
            flat_list.append(elem)
    return flat_list


def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """
    flattened = flatten_list(data)
    try:
        ips = [
            (flattened[idx + 1], flattened[idx + 3])
            for idx, val in enumerate(flattened)
            if val == "ip"
        ]
    except IndexError:
        return []
    valid_ips = []
    for tup in ips:
        if tup[0] is None or tup[1] is None:
            continue
        try:
            socket.inet_aton(tup[0].replace('"', ""))
        except OSError:
            continue
        valid_ips.append((tup[0].replace('"', ""), tup[1]))
    return valid_ips


l = [
    [
        "TEST",
        [
            "parent",
            [],
            "uuid",
            ['"khk-yyas4h-323223-wewe-343er-3434-www"'],
            "display_name",
            ['"services"'],
            "IPV4",
            [
                [
                    ["ip", ['"1.1.1.0"'], "mask", ["20"], "type", ["ip_mask"]],
                    ["ip", ['"2.2.2.2"'], "mask", ["32"], "type", ["ip_mask"]],
                ]
            ],
        ],
    ]
]

m = [["TEST", ["ip", ['"1.1.1.0"'], "mask", [None], "type", ["ip_mask"]], "id"]]

n = [["ip", "mask"]]

print(extract_ipv4(l))
