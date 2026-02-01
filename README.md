# Auto Number Scripts
## Setup
Run

    pip install pyautogui
## Entry
Adds parts to Monday sequentially
### Usage

    python sequential_entry.py --prefix "802-C0-P" --start 1 --end 4 --delay 5

| Parameter | Usage |
|--|--|
| --prefix | Start of part number sequence |
| --start | Start of number range |
| --end | End of number range |
| --delay | Starting delay |


## Rename
Renames parts in onshape
Make sure you are in onshape and hovering over the first part when you start it. expand the parts list so all are visible

    python sequential_rename.py --prefix "803-C0-P" --start 1 --end 4 --move 26
   

| Parameter | Usage |
|--|--|
| --prefix | Start of part number sequence |
| --start | Start of number range |
| --end | End of number range |
| --delay | Starting delay |
| --move | height of part items in onshape (px) 26 works well for me |
