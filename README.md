# Rename Files

Rename Files is a python script that takes directory paths as paths as
parameters. It renames all <strong>regular files</strong> within each given
directory to the naming convention below. It ignores all hidden files and
subdirectories in the the renaming process.

## Naming Convention
```
FOLDERNAME - # of COUNT
```
Where: </br>
- FOLDERNAME is the name of the directory
- \# is and incrementing integer from 1 to COUNT. (Files are sorted by date modified)
- COUNT is the number of regular files in the directory

## Usage
```
python3 rename.py path [paths]
```