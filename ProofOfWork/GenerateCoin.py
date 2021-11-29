from hashlib import md5
from random import choice
import concurrent.futures


def generate_string():
    while True:
        yield "".join([choice("0123456789") for i in range(50)])


def get_hash(string):
    hash = md5(string.encode('utf8')).hexdigest()
    if hash.endswith("00000"):
        print(string, hash)

    return string, hash


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(get_hash, generate_string())


if __name__ == "__main__":
    main()
