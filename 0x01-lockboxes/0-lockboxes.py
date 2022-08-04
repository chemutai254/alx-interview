#!/usr/bin/python3

"""
Determines whether a box can be unlocked
"""


def canUnlockAll(boxes):
    """Determines whether to unlock the boxes or not using matching keys """

 num_boxes = len(boxes)
  
  if num_boxes == 0:
       return False
   keys = set(boxes[0])
   unlocked_keys = 1
   next_lock = 0
   flag = 0

    while unlocked_keys < num_boxes:
        next_lock = next_lock + 1
        if next_lock == num_boxes:
            return True if flag == 0 else False
        if next_lock in keys:
            keys = keys.union(set(boxes[next_lock]))
            unlocked_keys = unlocked_keys + 1
            flag = 0
            continue
        else:
            flag = 1

    return True

""" for (i=0; i<=boxes; i++){
if (boxes % 2 == 0)
 return true;
 else:
return false;
}"""
