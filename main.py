def capitalize(text):
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


def main():
    capitalize("hello")


if __name__ == '__main__':
    main()