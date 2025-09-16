import sys

num_params = len(sys.argv) - 1

if num_params == 0:
    print("none")
else:
    print(f"parameters: {num_params}")
    
    params = sys.argv[1:]
    
    for param in params:
        print(f"{param}: {len(param)}")