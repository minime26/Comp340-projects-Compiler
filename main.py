'''
Course: COMP 340
Name: Mohammed Miahjee
Lexar works as expected.
Parser in process


'''

import Lexar as l
from Parser import parser

#Print result of parser
def printTree(treeRoot):
    if treeRoot.token == "NUMB":
        print(treeRoot.value,end="")
    else:
        print("(",end="")
        printTree(treeRoot.left)
        print(treeRoot.value,end="")
        printTree(treeRoot.right)
        print(")",end="")

lexar = l.Lexar()

sc = "1+3*4"

lexar = lexar.TOKENIZE(sc)
tree = parser(lexar)

print(lexar)

printTree(tree)




