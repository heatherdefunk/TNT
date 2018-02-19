# Trinitrotoluene programing language tokenizer!
# Written by Timothy Schoonover
# Based on Tachyon and FlowLang, languages originally developed by Ryan Maugin ---> https://ryanmaugin.github.io/

#Import other files
import re #Used for some stuff, I think
import main #So we can access the inputed data

class Lexer(object): #Creates Lexer class, which is used to find lexical analysis of the inputed data

    #Initiate the Lexer class!
    def __init__(self, code): #Creates an __init__ function with the inputes of self and code
        self.code = code #Creates code

    #Reserved Inputs (can't be used for variables)
    keywords = ["function", "null", "class", "if", "for", "else", "true", "false", "nil", "print", "bool", "int", "str"] #list of keywords
    functions = ["display", "ask"] #list of functions
    datatypes = ["bool", "int", "str"] #list of datatypes
    operators = ['+', '-', '*', '/', '%', '=', '==', '<=', '>=', '+=', '-=', '*=', '/=', '%=', '||', '&&'] #list of operators
    seperators = ['::']
    scope_definers = ['{}'] #Used to find the end of a statement


    #Creates the split code input
    '''
    Process of spliting:
    Turns "var a = 5;" into a list of:
    var
    a
    =
    5
    ;
    so we can work with it to find the tokens inside of it.
    '''
    line = content.split() #Turns the string into an array of strings. For example, 'var a = 5 ;'' would be turned into ['var', 'a', '=', '5', ';'] this will make it easier to work with.

    #Let's tokenize! Initiates Lexer information
    def tokenize(code): #Creates

        #Some basic definitions
        tokens = [] #this makes a list of the seperate tokens
        code = self.code.split() #Splits the code into organised, seperate words
        index = 0 #Which rotation are we on?

        #Loops through the whole code adding words as we go!
        while index < len(code): #Creates a while loop so that we iterate through the whole statement
            word = code[index] #Creates a variable so we can actually work with the different tokens

            #Let's get down to business to create the tokens (bad pun, I know)
            if word == "var": tokens.append(["VAR_DECLERATION", word]) # Adds var to the tokens array if it's var
            elif word in keywords: tokens.append(["KEYWORD", word]) # Adds KEYWORD to the tokens array if it's a keyword
            elif word in functions: tokens.append(["FUNCTION", word]) # Does the same as lines 31 and 32, but for functions
            elif word in datatypes: tokens.append(["DATATYPE", word]) # Same as 33, but for datatypes
            elif word in operators: tokens.append(["OPERATOR", word]) # Same as 34, but for operators
            elif word in seperators: tokens.append(["SEPERATOR", word]) # Same as 35, but for seperators
            elif word in scope_definers: tokens.append(["SCOPE_DEFINER", word]) # Same as 36, but for scope definers
            elif re.match('[a-z]', word) or re.match('[A-Z]', word): # If the input code is either a-z or A-Z, then...
                tokens.append(["IDENTIFIER", word]) # Adds IDENTIFIES to the tokens array if the input is a-z or A-Z
            elif re.match('[0-9]', word): # If the input code is a number: 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9...
                tokens.append(["INTEGER", word]) # Adds INTEGER to the tokens array
            else: print("FATAL ERROR WITH THE LEXICAL ANALOGY PROCESS. STANDBY.") # If none of these conditions are met, uht oh!

            index += 1 # This is so we can iterate through the whole code
        return tokens #Returns the list of tokens to the other files
