


from enum import Enum
from enum import auto
from enum import unique


@unique
class TokenType(Enum):

    """运算符和分隔符"""
    TK_PLUS = auto()                    # +   加号
    TK_MINUS = auto()                   # -   减号
    TK_STAR = auto()                    # *   乘号
    TK_DIVIDE = auto()                  # /   除号
    TK_MOD = auto()                     # %   求余运算符
    TK_EQ = auto()                      # ==  等号
    TK_NEQ = auto()                     # !=  不等号
    TK_LT = auto()                      # <   小于号
    TK_LEQ = auto()                     # <=  小于等于号
    TK_GT = auto()                      # >   大于号
    TK_GEQ = auto()                     # >=  大于等于号
    TK_ASSIGN = auto()                  # =   赋值运算符
    TK_POINTSTO = auto()                # -> 
    TK_DOT = auto()                     # .  
    TK_AND = auto()                     # &   地址与运算符
    TK_OR = auto()                      # |


    TK_FALSE = auto()                   # !


    TK_OPENPA = auto()                  # (   左圆括号
    TK_CLOSEPA = auto()                 # )   有圆括号
    TK_OPENBR = auto()                  # [   左中括号
    TK_CLOSEBR = auto()                 # ]   右中括号
    TK_BEGIN = auto()                   # {   左大括号
    TK_END = auto()                     # }   右大括号
    TK_SEMICOLON = auto()               # ;   分号
    TK_COMMA = auto()                   # ,   逗号
    TK_ELLIPSIS = auto()                # ... 省略号

    TK_EOF = auto()                     #文件结束符

    """标识符"""
    TK_IDENT = auto()       #标识符
    TK_NONE = auto()        #空

    """"""
    TK_CNUMBER = auto()     #
    TK_CCHAR = auto()       #
    TK_CSTR = auto()        #

    """关键字"""
    KW_VOID = auto()        # void关键字
    KW_SHORT = auto()       # short关键字
    KW_INT = auto()         # int关键字
    KW_LONG = auto()        # long关键字
    KW_FLOAT = auto()       # float
    KW_DOUBLE = auto()      # double
    KW_BOOL = auto()        # bool
    KW_CHAR = auto()        # char关键字
    KW_STRING = auto()      # string



token_type_dict = {
    "+":TokenType.TK_PLUS,
    "-":TokenType.TK_MINUS,
    "*":TokenType.TK_STAR,
    "/":TokenType.TK_DIVIDE,
    "%":TokenType.TK_MOD,
    "==":TokenType.TK_EQ,
    "!=":TokenType.TK_NEQ,
    "<":TokenType.TK_LT,
    "<=":TokenType.TK_LEQ,
    ">":TokenType.TK_GT,
    ">=":TokenType.TK_GEQ,
    "=":TokenType.TK_ASSIGN,
    "->":TokenType.TK_POINTSTO,
    ".":TokenType.TK_DOT,
    "&":TokenType.TK_AND,
    "|":TokenType.TK_OR,

    "!":TokenType.TK_FALSE,

    "+=":TokenType.TK_PLUS,
    "-=":TokenType.TK_MINUS,
    "*=":TokenType.TK_STAR,

    "++":TokenType.TK_PLUS,
    "--":TokenType.TK_MINUS,


    "(":TokenType.TK_OPENPA,
    ")":TokenType.TK_CLOSEPA,
    "[":TokenType.TK_OPENBR,
    "]":TokenType.TK_CLOSEBR,
    "{":TokenType.TK_BEGIN,
    "}":TokenType.TK_END,
    ";":TokenType.TK_SEMICOLON,
    ",":TokenType.TK_COMMA,
    "...":TokenType.TK_ELLIPSIS,

    "void":TokenType.KW_VOID,
    "short":TokenType.KW_SHORT,
    "int":TokenType.KW_INT,
    "long":TokenType.KW_LONG,
    "float":TokenType.KW_FLOAT,
    "double":TokenType.KW_DOUBLE,
    "bool":TokenType.KW_BOOL,
    "char":TokenType.KW_CHAR,
    "string":TokenType.KW_STRING,
};




class Token(object):
    
    """
    Token类。

    @ivar file: 文件名.
    @ivar ttype: token_type;

    """

    
    __slots__ = ["file","ttype","value","line","cols"];


    def __init__(self,file:str,ttype,value:str,line:int,cols:int):
        super().__init__();

        self.file = file;
        self.ttype = ttype;
        self.value = value;
        self.line = line;
        self.cols = cols;

    

    def print(self):
        print("File:" + str(self.file));
        print("Type:" + str(self.ttype));
        print("Value:" + str(self.value));
        print("Line:" + str(self.line));
        print("Cols:" + str(self.cols) + "\n");

    
    def write(self,fp):

        """
        #param fp: open()的返回值
        """

        fp.write("File:" + str(self.file) + "\n");
        fp.write("Type:" + str(self.ttype) + "\n");
        fp.write("Value:" + str(self.value) + "\n");
        fp.write("Line:" + str(self.line) + "\n");
        fp.write("Cols:" + str(self.cols) + "\n\n");
        



class TokenStream(object):




    def __init__(self,tokens:list = []):
        super().__init__()

        self.token = tokens;


    def print(self):
        for token in self.token:
            token.print();


    def write(self,file):
        fp = open(file,"w",encoding="UTF-8");
        fp.write("Log:\n");
        for token in self.token:
            token.write(fp);



    def append(self,token:Token):
        self.token.append(token);


    def __getitem__(self, index):

        if isinstance(index, slice):
            return self.token[index]
        
        if len(self.token) > index:
            return self.token[index]
        else:
            return None


    def __len__(self):
        return len(self.token)

    def __repr__(self):
        return repr(self.token)

    def __iter__(self):
        return iter(self.token)






















