import pickle
import os
import sys
import shutil

args = sys.argv



dir = os.path.normpath(args[1]) + os.sep
save_dir = os.path.normpath(args[2]) + os.sep

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

def get_changes(mapping, new_mapping):
    changes = []
    for file in mapping:
        if file not in new_mapping:
            changes.append(("deleted", file))
        elif mapping[file] != new_mapping[file]:
            changes.append(("modified", file))
    for file in new_mapping:
        if file not in mapping:
            changes.append(("added", file))
    return changes

def commit_changes(changes, save_dir):
    for change in changes:
        path = change[1].replace(os.path.expanduser(dir), os.path.expanduser(save_dir))
        if change[0] == "deleted":
            os.remove(path)
        elif change[0] == "modified":
            with open(change[1], "rb") as f:
                data = f.read()
            with open(path, "wb") as f:
                f.write(data)
        elif change[0] == "added":
            os.makedirs("/".join(path.split("/")[:-1]), exist_ok=True)
            shutil.copy2(change[1], path)

if __name__ == "__main__":
    files = get_every_file(dir)
    new_mapping = last_modified(files)
    with open(dir + "/state.pkl", "rb") as f:
        mapping = pickle.load(f)
    changes = get_changes(mapping, new_mapping)
    commit_changes(changes, save_dir)
    with open(dir + "/state.pkl", "wb") as f:
        pickle.dump(new_mapping, f)
        
