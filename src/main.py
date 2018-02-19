# trinitrotoluene programing language: putting it all together
# written by timothy schoonover

import lexer

def main():
    content = "" #creates a content variable
    with open('test.tnt', 'r') as file: #opens the test.tnt file to observe its code
        content = file.read() #reads the code in the test.tnt file
    lex = lexer.lexer(content) #initialize the lexer function
    tokens = lex.tokenize() #uses the tokenize function to create tokens

main()
