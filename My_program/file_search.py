#!/usr/bin/env python3
import os
import argparse
import fnmatch


def search_files(root, name_pattern=None, text_pattern=None):
    """Yield file paths under root matching name or containing text."""
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if name_pattern and not fnmatch.fnmatch(filename.lower(), name_pattern.lower()):
                continue
            path = os.path.join(dirpath, filename)
            if text_pattern:
                try:
                    with open(path, 'r', errors='ignore') as f:
                        if text_pattern not in f.read():
                            continue
                except Exception:
                    continue
            yield path


def main():
    parser = argparse.ArgumentParser(description="Simple file search utility")
    parser.add_argument('-d', '--dir', default='.', help='Directory to search')
    parser.add_argument('--name', help='Filename pattern (e.g. "*.txt")')
    parser.add_argument('--text', help='Search text within files')
    args = parser.parse_args()

    if not args.name and not args.text:
        parser.error('Specify --name and/or --text to search')

    for result in search_files(args.dir, args.name, args.text):
        print(result)


if __name__ == '__main__':
    main()
