#https://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("/Users/baonguyen/Pictures/photos"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)
