import sys

num_params = len(sys.argv) - 1

if num_params != 1:
    print("none")
else:
    param = sys.argv[1]
    
    z_found = ""

    for char in param:
        if char == 'z':
            z_found = z_found + "z"
            
    if len(z_found) > 0:
        print(z_found)
    else:
        print("none")