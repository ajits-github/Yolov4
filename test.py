def main(things, option_a, option_n):
    print(locals())  # Debugging 


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("things", help="Bla bla", nargs="*")
parser.add_argument("-o", "--option-a", help="Bla bla", default="Op A")
parser.add_argument("-n", "--option-n", help="Ble ble", default="Op N")
args = parser.parse_args()

# The only difference and the magic sauce...
print(vars(args))  

# main(
#     things=args.things,
#     option_a=args.option_a,
#     option_n=args.option_n
# )