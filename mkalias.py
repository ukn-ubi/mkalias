import sys

try:
    shell = sys.argv[1]
    alias = sys.argv[2]
    run = sys.argv[3]

    run = run.replace('"', "")
    run = run.replace("'", "")
except:
    print("Usage: \n\tmkalias <shell> <alias> <command>")
    sys.exit()

if shell == "zsh" or shell == "bash" or shell == "sh":
    print("alias " + alias + "=\"" + run + "\"")
elif shell == "fish":
    print("alias " + alias + " \"" + run + "\"")
else:
    print("Sorry you're shell isn't supported. Please submit a issue on Github and I will try to include it.")
