def flatten(list_of_lists):
    flat_list = []

    # Inspect each element in the list, this could be a function
    for list_element in list_of_lists:

        # If a list extend the flat list
        if isinstance(list_element, list):
            flat_list.extend(list_element)

        # If a tuple convert to list and extend the flat list
        elif isinstance(list_element, tuple):
            flat_list.extend(list(list_element))

        # A non list / tuple just append to the flat list
        else:
            flat_list.append(list_element)

    # Now recursively iterate to find further nesting
    for flat_list_element in flat_list:
        if isinstance(flat_list_element, (list, tuple)):
            return flatten(flat_list)

    return flat_list
