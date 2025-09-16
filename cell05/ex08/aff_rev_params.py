import sys

num_params = len(sys.argv) - 1

if num_params < 2:
    print("none")
else:
    params = sys.argv[1:]
    for param in params[::-1]:
        print(param)