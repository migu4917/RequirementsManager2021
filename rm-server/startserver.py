from subprocess import call
import platform
import sys
from multiprocessing import Pool
from multiprocessing import Process
import subprocess
import os
from threading import Thread

# import gateway.main
# import usermanager.main
# import projectmanager.main
# import requirementmanager.main

serverCmds = [
    "python gateway/gateway/main.py flask",
    "python usermanager/usermanager/main.py flask",
    #"python projectmanager/projectmanager/main.py flask",
    #"python requirementmanager/requirementmanager/main.py flask",
    "python templatemanager/templatemanager/main.py flask",
]

# def startServe(cmd):
#     # os.system(cmd)
#     subprocess.run(args=cmd, shell=True, encoding="utf-8")

if __name__ == "__main__":
    for cmd in serverCmds:
        os.system("cmd.exe /c start cmd.exe /c\"" + cmd + "\"")
    pass

# #!/usr/bin/env python
# """Continuation-passing style (CPS) script.

# Usage:

#    $python cps.py script1.py arg1 arg2 -- script2.py a b c -- script3.py ...
# """

# if len(sys.argv) < 2:
#     sys.exit()  # nothing to do

# # define a command that starts new terminal
# if platform.system() == "Windows":
#     new_window_command = "cmd.exe /c start cmd.exe /c".split()
# else:  # XXX this can be made more portable
#     new_window_command = "x-terminal-emulator -e".split()

# # find where script args end
# end = sys.argv.index('--') if '--' in sys.argv else len(sys.argv)

# # call script; wait while it ends; ignore errors
# call([sys.executable] + sys.argv[1:end])

# # start new window; call itself; pass the rest; ignore errors
# rest = sys.argv[end+1:]
# if rest:
#     call(new_window_command + [sys.executable, sys.argv[0]] + rest)

# print("Press Enter to exit")  # NOTE: to avoid raw_input/input py3k shenanigans
# sys.stdin.readline()
