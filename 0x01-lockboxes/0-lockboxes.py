#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    unlocked = set()

    def dfs(box):
        '''recursive dfs function'''
        if box in unlocked:
            return
        unlocked.add(box)
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                dfs(key)

    dfs(0)
    return len(unlocked) == len(boxes)
