import sys
params = sys.argv[1:]
if len(params) != 2:
    print("none")
else:
    try:
        start = int(params[0])
        end = int(params[1])
        arr = list(range(start, end + 1))
        print(arr)
    except ValueError:
        print("none")