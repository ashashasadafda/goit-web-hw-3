from threading import Thread

import shutil
from pathlib import Path, PurePath

from time import time


source_dir = Path('./picture')
dist = Path('./dist')


def sort_file(file):
    pure_p = PurePath(file)
    suffix = pure_p.suffix[1:]
    print(suffix)

    file_path = dist / suffix
    # print(file)
    try:
        file_path.mkdir(parents=True, exist_ok=True)
        shutil.copy(file, file_path)
    except FileExistsError:
        print("File already exists")


if __name__ == '__main__':
    start = time()

    for filepath in source_dir.rglob('*'):
        if filepath.is_file():
            # print(filepath)
            thread = Thread(target=sort_file, args=(filepath,))
            thread.start()
            thread.join()

    print(f'time spent: {start - time()}')
