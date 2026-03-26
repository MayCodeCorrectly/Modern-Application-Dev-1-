# When you execute python file using terminal given arguments can be accessed using sys.argv
import sys

cmd_args = sys.argv

for arg in cmd_args:
    print(arg)

# 0th index --> file name 
    # python cmd_args.py hi how are you yup this will get print too ?