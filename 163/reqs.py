from collections import namedtuple

Package = namedtuple("Package", "name version")


def _process_package(requirement):
    package, version = requirement.split("==")
    return Package(package, [int(n) for n in version.split(".")])


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old_reqs_dict = dict(
        [_process_package(line) for line in old_reqs.split("\n") if line != ""]
    )
    new_reqs_dict = dict(
        [_process_package(line) for line in new_reqs.split("\n") if line != ""]
    )

    return [
        package
        for package in old_reqs_dict.keys()
        if new_reqs_dict[package] > old_reqs_dict[package]
    ]
