#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc != 1 else ""))

        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i + 1]))
