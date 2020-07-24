



from .token import *




class Lexer(object):



    def __init__(self,file):
        super().__init__()

        self.line = 1;
        self.cols = 0;

        self.file = file;
        self.fp:TextIOWrapper = open(file,"r",encoding="UTF-8");
        self.source:str = self.fp.read();
        self.source_length = len(self.source);
        self.cursor = -1;

        self.token:TokenStream = TokenStream();
        

    def match(self, regexp):
        """
        Matches something at the current position, skipping past
        whitespace. Even if we can't match, the current position is
        still skipped past the leading whitespace.
        """

        self.skip_whitespace()
        return self.match_regexp(regexp)


    def next_line(self):

        self.line += 1;
        self.cols = 0;

        if self.cursor < self.source_length:
            ch = self.source[self.cursor];
            while ch != "\n":
                self.cursor += 1;
                if self.cursor < self.source_length:
                    ch = self.source[self.cursor];
                else:
                    break;
                if ch == '':
                    break;






    def next_ch(self,offset:int = 1) -> str:

        """
        @param offset: 用1或-1
        """

        self.cols += offset;
        self.cursor += offset;

        if self.cursor < self.source_length:
            ch = self.source[self.cursor];
        else:
            return '';
            
        
        return ch;
        


    def print(self):
        self.token.print();


    def write(self,file):
        self.token.write(file);


    def lex(self):
        self.line = 1;
        self.cols = 0;

        self.fp = open(self.file,"r",encoding="UTF-8");
        self.source:str = self.fp.read();
        self.source_length = len(self.source);
        self.cursor = -1;


        lex = True;

        while lex:
            ch:str = self.next_ch();

            
            if ch == '' or ch == None:
                break;
            elif ch == "\n":
                self.next_line();
            elif ch == " ":
                continue;
            

            #加减
            if ch in ("+","-"):
                next_ch = self.next_ch(1);
                if next_ch == "=":
                    self.token.append(Token(self.file,token_type_dict[ch],ch + next_ch,self.line,self.cols - 1));
                elif next_ch in ("+","-"):
                    self.token.append(Token(self.file,token_type_dict[ch],ch + next_ch,self.line,self.cols - 1));
                else:
                    self.next_ch(-1);
                    self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));

            

            elif ch in ("<",">","!","="):
                next_ch = self.next_ch(1);
                if next_ch == "=":
                    self.token.append(Token(self.file,token_type_dict[ch + next_ch],ch + next_ch,self.line,self.cols - 1));
                else:
                    self.next_ch(-1);
                    self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));
            

            #注释
            elif ch == "/":
                next_ch = self.next_ch(1);
                if next_ch == "/":#单行注释
                    self.next_line();
                elif next_ch == "*":#注释块

                    star_line = self.line;
                    star_cols = self.cols;

                    while True:
                        star = self.next_ch();

                        if star == "*" and self.next_ch() == "/":
                            ch = self.next_ch();
                            if ch == "\n":
                                self.next_line();
                            break;
                        elif star == '':#EOF
                            print("\nFile:" + str(self.file));
                            print("Line:" + str(star_line));
                            print("Cols:" + str(star_cols - 1));
                            print("  /*");
                            print("  ^^");
                            print("error\n");
                            lex = False;
                            break;
                else:
                    self.next_ch(-1);
                    self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));
            

            #符号
            elif ch in ("(",")","[","]","{","}",",",";"):
                self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));


            #省略号
            elif ch == ".":
                next_ch = self.next_ch();
                if next_ch == ".":
                    next_ch = self.next_ch();
                    if next_ch == ".":
                        self.token.append(Token(self.file,token_type_dict["..."],"...",self.line,self.cols));
                    else:
                        self.next_ch(-2);
                        self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));
                else:
                    self.next_ch(-1);
                    self.token.append(Token(self.file,token_type_dict[ch],ch,self.line,self.cols));
                


            #标识符
            elif ch.isalpha() or ch == "_":
                value = ch;
                ch = self.next_ch(1);
                while ch.isalpha() or ch == "_":
                    value += ch;
                    ch = self.next_ch(1);
                

                if value in token_type_dict:
                    self.token.append(Token(self.file,token_type_dict[value],value,self.line,self.cols - len(value)));
                else:
                    self.next_ch(-1);
                    self.token.append(Token(self.file,TokenType.TK_IDENT,value,self.line,self.cols - len(value) + 1));
                

            
            #数字
            elif ch.isnumeric():
                value = ch;
                ch = self.next_ch(1);
                while ch.isnumeric():
                    value += ch;
                    ch = self.next_ch(1);
                
                self.next_ch(-1);
                self.token.append(Token(self.file,TokenType.TK_CNUMBER,value,self.line,self.cols - len(value) + 1));



            
            #字符串
            elif ch == "\'" or ch == "\"":
                
                str_line = self.line;
                str_cols = self.cols;

                next_ch = self.next_ch(1);
                value = next_ch;

                while True:
                    
                    next_ch = self.next_ch(1);


                    if next_ch == ch:
                        self.token.append(Token(self.file,TokenType.TK_CSTR,value,self.line,self.cols - len(value) + 1));
                        break;
                    elif next_ch == '' or next_ch == "\n":
                        print("\nFile:" + self.file)
                        print("Line:" + str(str_line));
                        print("Cols:" + str(str_cols));
                        print("  " + ch);
                        print("  ^");
                        print("error\n");
                        lex = False;
                        break;
                    else:
                        value += next_ch;

            
            
            

            


                            

            



                    

                    



                






















