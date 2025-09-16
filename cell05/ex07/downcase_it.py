import sys

num_params = len(sys.argv) - 1

if num_params == 1:
    param = sys.argv[1]
    print(param.lower())
else:
    print("none")