import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage python pink.py <filename>")
    filename = sys.argv[1]
    print(filename)

    with open(filename) as file:
        source = file.read()
        print(source)

        # TODO: Tokenize the input source
