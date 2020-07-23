


from lexer.lexer import *
import parser




def main():
    lexer = Lexer("./test.txt");
    lexer.lex();
    lexer.write("./log.txt");
    lexer.print();




if __name__ == "__main__":
    main();


