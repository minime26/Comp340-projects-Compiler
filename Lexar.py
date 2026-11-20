'''
File name: Lexar.py
Description: Takes an expression -> creates a list of lists [char, type]

'''


class Lexar:

    def __init__(self):
        self.NUMB = ['0','1','2','3','4','5','6','7','8','9']
        self.PLUS = '+'
        self.MINUS = '-'
        self.MULTI = '*'
        self.DIVIDE = '/'
        self.L_PARAN = '('
        self.R_PARAN = ')'





    def TOKENIZE(self,sc):
        scl = []
        for i in sc:          #i = sc
            if i in self.NUMB:       #if i is a number
                if not scl or scl[-1][1] != "NUMB":         #if scl is empty or if last element is not a number
                    scl.append([i, "NUMB"])     #append i to scl
                    continue
                else:           #else if last element is a number
                    scl[-1] = [scl[-1][0]+i, "NUMB"]    #concatenate i+last
                    continue

            elif i == self.PLUS:
                scl.append([i, "PLUS"])     #append i to scl
            elif i == self.MINUS:
                scl.append([i, "MINUS"])
            elif i == self.MULTI:
                scl.append([i, "MULTI"])     #append i to scl
            elif i == self.DIVIDE:
                scl.append([i, "DIVIDE"])     #append i to scl
            elif i == self.L_PARAN:
                scl.append([i, "L_PARAN"])     #append i to scl
            elif i == self.R_PARAN:
                scl.append([i, "R_PARAN"])     #append i to scl

        return scl      #return list of tokens
    #---




    #=-======================================
