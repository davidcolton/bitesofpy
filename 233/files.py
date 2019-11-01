from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path("/tmp")
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def zip_last_n_files(
    directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3
):
    log_path = Path(directory)
    # Create list of tuples
    # (modified_time, log_file, new_log_file)
    list_of_files = []
    for log_file in log_path.iterdir():
        if log_file.is_file():
            mod_time = datetime.fromtimestamp(log_file.stat().st_mtime)
            # Hack assumes a .log extension or at least '.xxx' format
            new_log_file = PosixPath(
                f"{str(log_file)[:-4]}_{mod_time.strftime('%Y-%m-%d')}{str(log_file)[-4:]}"
            )
            list_of_files.append((mod_time, log_file, new_log_file))

    list_of_files = sorted(list_of_files, reverse=True)

    # Now zip up n files
    with ZipFile(zip_file, "w") as zipf:
        for file_to_zip in list_of_files[:n]:
            source = file_to_zip[1]
            destination = file_to_zip[2]
            zipf.write(source, destination.name)
