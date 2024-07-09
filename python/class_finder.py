from pathlib import Path
import re

user_input = input('wats the name of the class: ')


def get_info() -> str:
    location = Path(r'C:\Users\Admin\Desktop\target.txt')
    with open(location) as file:
        reader = file.read()
        return reader


def split_info() -> list:
    info = get_info()
    split_pattern = re.compile(r'\n', flags=re.MULTILINE | re.IGNORECASE)

    return re.split(split_pattern, info)


def is_match(info: str) -> bool:
    pattern = re.compile(rf'.*{user_input}.*')

    if pattern.match(info.lower()):
        return True

    return False


def match_class() -> str:
    info = split_info()
    matches = []

    for line in info:
        if is_match(line):
            matches.append(line)

    return '\n' + '\n'.join(matches)


def final_output(*, clean: bool = False):
    matches: str = match_class()
    if clean:
        pattern = re.compile(r'[\s{:\[>\n+*=(,@)"}\];!]')

        cleaned_matches = sorted(set(re.split(pattern, matches)))

        return (

            '\n'.join(cleaned_matches)
            .replace('\n' * 2, '\n')
            .replace('\n' * 3, '\n')
            .replace('\n' * 4, '\n')
            .replace('\n' * 5, '\n')

        )

    return matches


def main():
    try:
        print(final_output(clean=True))
    except KeyboardInterrupt:
        print('you have quit')


if __name__ == '__main__':
    main()
