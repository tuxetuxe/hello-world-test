import argparse


def greeting(name=None):
    return f"Hello {name}!" if name else "Hello World!"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="?")
    parser.add_argument("--shout", action="store_true", help="print in capitals")
    args = parser.parse_args(argv)
    text = greeting(args.name)
    print(text.upper() if args.shout else text)


if __name__ == "__main__":
    main()
