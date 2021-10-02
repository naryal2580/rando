#!/shebang

from os import path, getcwd, get_terminal_size
from random import choice
from csv import DictReader
from stoyled import *


FILENAME = 'quotes.csv'
G4I = f'''{bold}   _   _
  ((___))
 [| o x |]
   \   /
   ('_')
'''

G4I = G4I.replace('o', f'{green_l}{bold}o{rst}{bold}{bold}')
G4I = G4I.replace('x', f'{red}{bold}x{rst}{bold}')
G4I = G4I.replace('_', f'{dim}_{rst}{bold}')
G4I = G4I.replace('(', f'{dim}({rst}{bold}')
G4I = G4I.replace(')', f'{dim}){rst}{bold}')
G4I = G4I.replace('/', f'{dim}/{rst}{bold}')
G4I = G4I.replace('\\', f'{dim}\\{rst}{bold}')
G4I += rst


def _print(content, flush=True):
    print(content, end='', flush=flush)


def read(filename, delimiter=';'):
    contents = []
    if path.isfile(filename):
        file = open(filename)
        reader = DictReader(file, delimiter=delimiter)
        # columns = reader.fieldnames
        for rows in reader:
            contents.append(rows)
        return tuple(contents)
    else:
        raise FileNotFoundError(f'{filename} doesn\'t exist.')


def get_categories(contents):
    categories = set()
    for content in contents:
        categories.add(content['category'])
    return tuple(categories)


def filter_category(contents, categories=('technology','time','work','science','power')):
    filtered_contents = []
    for content in contents:
        if content['category'] in categories:
            filtered_contents.append(content)
    return tuple(filtered_contents)


def main():
    # exit(0)
    filename = path.join(path.dirname(__file__), FILENAME)
    quotes = read(filename)
    filtered_quotes = filter_category(quotes)
    quote = choice(filtered_quotes)
    _print(G4I)
    print(f' "{quote["quote"]}" --{quote["author"]} ({quote["category"]})')


if __name__ == '__main__':
    main()
