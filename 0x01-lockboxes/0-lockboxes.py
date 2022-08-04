#!/usr/bin/python3

"""
Determines whether a box can be unlocked
"""


def canUnlockAll(boxes):
    """Determines whether to unlock the boxes or not using matching keys """

 unlocked = [0]
    for box_num, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_num:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False

""" for (i=0; i<=boxes; i++){
if (boxes % 2 == 0)
 return true;
 else:
return false;
}"""
