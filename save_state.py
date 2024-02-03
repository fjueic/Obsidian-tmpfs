import os
import pickle
import sys
args = sys.argv
'''
if len(args) != 2:
    print("Usage: python save_state.py <dir>")
    sys.exit(1)
'''
dir = os.path.normpath(args[1]) + os.sep 

def get_every_file(dir):
    files = []
    for root, dirs, filenames in os.walk(dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    if  dir + "state.pkl" in files:
        files.remove(dir + "state.pkl")
    return files 


def last_modified(files):
    mapping = {}
    for file in files:
        mapping[file] = os.path.getmtime(file)
    return mapping

def save_state(mapping, dir):
    with open(dir + "/state.pkl", "wb") as f:
        pickle.dump(mapping, f)

if __name__ == "__main__":
    files = get_every_file(dir)
    mapping = last_modified(files)
    save_state(mapping, dir) 
    
