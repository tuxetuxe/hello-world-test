import sys


def greeting(name=None):
    return f"Hello {name}!" if name else "Hello World!"


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    print(greeting(args[0] if args else None))


if __name__ == "__main__":
    main()
