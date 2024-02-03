# Obsidian-tmpfs

### [Is Obsidian Going to Kill My SSD?](https://www.reddit.com/r/ObsidianMD/comments/13j5j7p/is_obsidian_going_to_kill_my_ssd_some_calculations/)

From the conclusion of the above link, it's not going to kill your SSD, but it might wear it out faster than normal usage.

While using tmpfs for Obsidian might be considered overkill, it can be a fun experiment.

### How Does It Work?

- Create a `tmpfs` mount point within Obsidian's vault directory and configure Obsidian to use it as its vault.
- Copy the files from the original vault to the tmpfs mount point.
- When you're done with Obsidian, copy the files back to the original vault.
- Optionally, use `cronie` to automate this process at specific times.
- Note: It's recommended not to store attachments in tmpfs since they are unlikely to be edited. You can either create or delete them.

### How to Install?

- Currently, there isn't an automated script for installation; you need to do it manually.
- For the average user, using Obsidian as is without this setup is recommended, as the effort might not be worth it.
- If you're a power user interested in manual setup, I've provided some scripts to assist you. Feel free to reach out if you need help.

#### Provided Scripts:

- [mount_notes_fs.sh](./mount_notes_fs.sh): Creates a tmpfs mount point and copies files from the original vault to the tmpfs mount point. The original location and tmpfs mount point are hardcoded in the script. It also uses [save_state.py](./save_state.py) to save the last modified time of files in the tmpfs mount point.

- [save_state.py](./save_state.py): Saves the last modified time of files in the tmpfs mount point. Takes the tmpfs mount location as argument and saves the last modified time of files in a file called `state.pkl`.

- [save_changes.py](./save_changes.py): Copies the files that have been changed in the tmpfs mount point back to the original vault and update state.pkl. Takes the tmpfs mount location and the original vault location as arguments.
  
- Unmounting:- 
    1.  50MB of RAM is nothing.
    2.  I know you can figure it out if you were able to follow the above steps.

Using the [shell commands extension](https://github.com/Taitava/obsidian-shellcommands), you can run these scripts directly from Obsidian. Example:- tmpfs is mounted when Obsidian starts and unmounted when Obsidian closes.