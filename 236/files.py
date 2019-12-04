from pathlib import PosixPath, Path
from difflib import SequenceMatcher

SIMILAR = 0.6


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
    """Get all file names in "directory" and (case insensitive) match the ones
       that exactly match "filter_str"

       In case there is no exact match, return closely matching files.
       If there are no closely matching files either, return an empty list.
       (Return file names, not full paths).

       For example:

       d = Path('.')
       files in dir: bite1 test output

       get_matching_files(d, 'bite1') => ['bite1']
       get_matching_files(d, 'Bite') => ['bite1']
       get_matching_files(d, 'pybites') => ['bite1']
       get_matching_files(d, 'test') => ['test']
       get_matching_files(d, 'test2') => ['test']
       get_matching_files(d, 'output') => ['output']
       get_matching_files(d, 'o$tput') => ['output']
       get_matching_files(d, 'nonsense') => []
    """

    def _get_files_list(directory: PosixPath) -> list:

        filename_list = []

        file_iterator = Path(directory).iterdir()

        for entry in file_iterator:
            if entry.is_file():
                # print(entry.name)
                filename_list.append(entry.name)

        return filename_list

    files = _get_files_list(directory)

    if filter_str in files:
        return [filter_str]
    else:
        return [
            word
            for word in files
            if SequenceMatcher(None, word, filter_str).ratio() >= SIMILAR
        ]


print(get_matching_files(".", "files.py"))

