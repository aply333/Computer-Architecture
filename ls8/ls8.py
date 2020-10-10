#!/usr/bin/env python3

# """Main."""

# import sys
# from cpu import *

# def main(argv):
#     if len(argv) != 2:
#         print("Requires an input")
#         return 1
#     cpu = CPU()
#     cpu.load()
#     cpu.run()
#     return 0


# if len(sys.argv) != 2:
#     print("Incorrect Usage")
#     sys.exit(1)
    
# cpu = CPU()
# cpu.load(sys.argv[1])
# cpu.run()


import sys
from cpu import *

def main(argv):
    """Main."""
    if len(argv) != 2:
        print(f"usage: {argv[0]} filename", file=sys.stderr)
        return 1

    cpu = CPU()

    cpu.load(argv[1])

    cpu.run()

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))