#!/shebang

from os import path, getcwd, get_terminal_size
from textwrap import wrap as textwrap
from random import choice
from csv import DictReader
from stoyled import *


FILENAME = 'quotes.csv'
G41 = f'''   _   _
  ((___))
 [| o x |]
   \   /
   ('_')
'''

G4I = G41.replace('o', f'{green_l}{bold}o{rst}', 1)
G4I = G4I.replace('x', f'{red}{bold}x{rst}', 1)
# G4I = G4I.replace('_', f'{dim}_{rst}')
# G4I = G4I.replace('(', f'{dim}({rst}')
# G4I = G4I.replace(')', f'{dim}){rst}')
# G4I = G4I.replace('/', f'{dim}/{rst}')
# G4I = G4I.replace('\\', f'{dim}\\{rst}')


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


def get_cols():
    return get_terminal_size().columns


def wrap(text, up=False, lcols=16):
    return textwrap(text, get_cols() - 18)


def print_gai(quote):
    gai, quote = G4I.rstrip().split('\n'), tuple(quote[:3])
    if len(quote) == 1:
        quote = ('', quote[0], '')
    elif len(quote) == 2:
        quote = (quote[0], quote[1], '')
    if len(quote[-1]) >= get_cols() - 8:
        quote = (quote[0], quote[1], quote[2][:get_cols() - 8] + '...')
    line_len = -1
    for _ in quote:
        _ = len(_)
        if _ > line_len:
            line_len = _
    round_line_len = round(line_len/3.14)
    u = (7, 5, 1, 5, 6)
    b = (
            # '.'*(get_cols() - 18),
            '.'*line_len,
            '/ ' + italic + quote[0] + rst,
            '__/ ' + italic + quote[1] + rst,
            '\\ '+ italic + quote[2] + rst,
            '\\' + '_'*(round_line_len*2)
            )
    for i, j in enumerate(gai):
        print(f'{j}{" "*u[i]}{b[i]}')
    print()


def main():
    filename = path.join(path.dirname(__file__), FILENAME)
    quotes = read(filename)
    filtered_quotes = filter_category(quotes)
    quote = choice(filtered_quotes)
    fancy_quote = f' "{quote["quote"]}" --{rst}{bold}{quote["author"]}{rst} ({uline}{quote["category"]}{rst})'
    print_gai(wrap(fancy_quote))


if __name__ == '__main__':
    main()
