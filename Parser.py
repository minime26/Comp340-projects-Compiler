'''
File name: Parser.py
Description: Accepts a list from Lexar -> returns the root node of the created tree.

'''

class TreeNode:
    def __init__(self, value):
        self.value = value[0]
        self.left = None
        self.right = None
        self.token = value[1]





def parser(sc):
    if not sc: return None     #return if empty

    if len(sc) == 1:        #return sc if 1 element
        a = TreeNode(sc[0])
        return a

    if len(sc) >= 2:            #1+3-1 -> root=(+) | r.left=(1) | r.right=(3-1)
        b = TreeNode(sc[1])
        c = TreeNode(sc[0])
        b.left = c
        b.right = parser(sc[2:])
        return b
    return None



