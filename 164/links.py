import sys
import fileinput


INTERNAL_LINKS = ("pybit.es", "codechalleng.es")


def make_html_links():
    with fileinput.input() as f_input:
        lines = [line for line in f_input]
    for line in lines:
        line_parts = str(line).split(",")
        target = (
            ' target="_blank"'
            if not any(il in line_parts[0] for il in INTERNAL_LINKS)
            else ""
        )
        if line_parts[0].strip().startswith("http") and len(line_parts) == 2:
            print(
                f'<a href="{line_parts[0].strip()}"{target}>{line_parts[1].strip()}</a>'
            )


if __name__ == "__main__":
    make_html_links()
