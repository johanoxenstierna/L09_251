

"""Counts number of instances"""

import os

namesf = ['instancesL']

N = 0
for namef in namesf:
    path = './' + namef
    _, folders, _ = os.walk(path).__next__()
    N += len(folders)

print("There are " + str(N) + " instances.")