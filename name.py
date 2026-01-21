import sys
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Please provide a name as a command line argument.")

for name in sys.argv[1:-1]:
    print("hello, my name is " , name)


