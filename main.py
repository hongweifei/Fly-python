


from compiler.lexer import *
from compiler.parser import *

from sys import argv


def main():

    argc = len(argv);

    if argc == 1:
        print("Please specify an input file.");
    elif argc > 1:
        lexer = Lexer(argv[1]);
        lexer.lex();
        lexer.write("./log.txt");
        lexer.print();

        parser = Parser(lexer.token);
        parser.parse();
        parser.print();





if __name__ == "__main__":
    main();


