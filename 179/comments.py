import string
import re

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''


def _strip_comments_simple(code):
    return re.sub(r"#.*\n", "", code)
    """cleaned_code = ""
    for line in code.split("\n"):
        if not line.strip().startswith("#"):
            cleaned_code = cleaned_code + line + "\n"
    return str(cleaned_code)"""


def _strip_comments_docstring(code):
    return re.sub(r'\s*""".*"""', "", code, re.DOTALL)


def _strip_comments_inline(code):
    return re.sub(r"\s\s#.*\n$", "", code)
    """cleaned_code = ""
    for line in code.split("\n"):
        if line.find("  #"):
            index = line.find(r"  #")
            cleaned_code += f"{line[:index]}\n"
        else:
            cleaned_code = cleaned_code + line + "\n"
    return cleaned_code"""


def strip_comments(code):
    # see Bite description
    code = _strip_comments_simple(code)
    code = _strip_comments_inline(code)
    code = _strip_comments_docstring(code)
    print(code)


strip_comments(code_bite_description)
