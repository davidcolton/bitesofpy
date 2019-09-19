import string
import re


def strip_comments(code):
    # see Bite description
    cleaned_code = []
    in_docstring = 0
    for line in code.split("\n"):

        # Not currently in a docstring or multi-line comment
        if in_docstring % 2 == 0:

            # Simple comment at start of line
            if re.search("^[\s]*#.*$", line):
                # ignore
                next

            # Comments mid-line
            elif line.find("  #") > 0:
                index = line.find("  #")
                cleaned_code.append(line[:index])

            # Strip single line docstring
            elif len(re.findall('"""', line)) == 2:
                # ignore
                pass

            # A single line docstring
            elif len(re.findall('"""', line)) == 2:
                # ignore
                pass

            # The opening marker for docstring or multi-line comment
            elif len(re.findall('"""', line)) == 1:
                # ignore
                in_docstring += 1
                pass

            else:
                cleaned_code.append(line)

        elif in_docstring % 2 == 1:
            if len(re.findall('"""', line)) == 1:
                # ignore
                in_docstring += 1
                pass

    return "\n".join(cleaned_code)
