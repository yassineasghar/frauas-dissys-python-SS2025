# Exercise 2.3: File I/O - Reading and Writing

def read_text_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def reverse_text(text: str) -> str:
    _text = text.split()
    _text.reverse()
    return ' '.join(_text)


def write_text_to_file(file_path: str, text: str) -> None:
    with open(file_path, 'w') as file:
        file.write(text)


def main() -> None:
    file_path = 'files/example.txt'
    original_text = read_text_file(file_path=file_path)
    print(f'Contents of: {file_path} is:\n{original_text}')

    new_file_path = 'files/example_reversed.txt'
    reversed_text = reverse_text(original_text)
    print(f'Reversed Contents of: {file_path} is:\n{reversed_text}')

    write_text_to_file(file_path=new_file_path, text=reversed_text)


if __name__ == '__main__':
    main()
