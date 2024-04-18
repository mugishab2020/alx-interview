#!/usr/bin/python3
""" module for making the boxes unlocker"""
def canUnlockAll(boxes):
    """Check if it's possible to unlock all boxes in a given list of boxes"""
    opened = [0]
    for a in opened:
        for key in boxes[a]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(boxes) == len(opened):
        return True
    return False