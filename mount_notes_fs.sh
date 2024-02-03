#!/bin/sh

mount_point="$HOME/Obsidian/Notes/"
notes_dir="$HOME/Videos/Notes/"

# if Notes is not empty, exit
if [ "$(ls -A $mount_point)" ]; then
    echo "Notes is not empty, possibly already mounted"
    exit 1
fi

if [ ! -d "$mount_point" ]; then
    mkdir -p "$mount_point"
fi


# Create a tmpfs mount point
pkexec mount -t tmpfs -o size=50M tmpfs "$mount_point"

# Copy the notes to the tmpfs mount mount_point
cp -r "$notes_dir"* "$mount_point"
 
python ~/.config/hypr/script/obsidian/save_state.py "$mount_point"

