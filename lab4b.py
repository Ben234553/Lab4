#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2, removing duplicates
    return list(set(l1).union(set(l2)))

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return [item for item in l1 if item in l2]

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all values which are not shared between both lists (symmetric difference)
    return list(set(l1).symmetric_difference(set(l2)))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 0, -1, -2]
    
    print('list1:', list1)
    print('list2:', list2)
    print('join:', join_lists(list1, list2))
    print('match:', match_lists(list1, list2))
    print('diff:', diff_lists(list1, list2))
