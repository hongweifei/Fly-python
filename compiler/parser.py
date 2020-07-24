


from .ast import *
from .token import *





class ParseError(Exception):

    def __init__(self, file, number, msg, line = None, cols = None, first = False):
        message = u"File \"%s\", line %d: %s" % (file, number, msg);

        if line:
            if isinstance(line, list):
                line = "".join(line)

            lines = line.split('\n')

            if len(lines) > 1:
                open_string = None
                i = 0

                while i < len(lines[0]):
                    c = lines[0][i]

                    if c == "\\":
                        i += 1
                    elif c == open_string:
                        open_string = None
                    elif open_string:
                        pass
                    elif c == '`' or c == '\'' or c == '"':
                        open_string = c

                    i += 1

                if open_string:
                    message += "\n(Perhaps you left out a %s at the end of the first line.)" % open_string

            for l in lines:
                message += "\n    " + l

                if cols is not None:
                    if cols <= len(l):
                        message += "\n    " + " " * cols + "^"
                        cols = None
                    else:
                        cols -= len(l)

                if first:
                    break

        self.message = message

        Exception.__init__(self, message)

    def __unicode__(self):
        return self.message





class Parser(object):
    


    def __init__(self,stream:TokenStream):
        super().__init__()

        self.cursor = -1;
        self.stream = stream;
        
        self.tree = [];
        
        self.var = {};
        self.func = {};
        self.user_class = {};



    def parse(self):

        
        self.cursor += 1;
        if self.cursor < len(self.stream):
            token:Token = self.stream[self.cursor];
        else:
            return;


        if token.ttype == TokenType.TK_SEMICOLON:
            self.parse()


        # 变量和函数
        if token.value in var_dict:
            root = RootNode(token);     #根节点

            self.cursor += 1;
            ident:Token = self.stream[self.cursor];
            self.cursor += 1;
            next_token:Token = self.stream[self.cursor];
                
            ident_node = Node(ident);       # 标识符
            next_node = Node(next_token);   # 运算符

            if ident.ttype == TokenType.TK_IDENT:
                if next_token.ttype == TokenType.TK_OPENPA:     # 声明函数
                    root.ttype = TreeType.FUNCTION
                elif next_token.ttype == TokenType.TK_ASSIGN:   # 声明变量
                    root.ttype = TreeType.VAR;
                else:
                    self.cursor -= 2;
                    return;


            # 声明变量
            if root.ttype == TreeType.VAR and ident.value not in self.var:
                root.add_child(next_node)
                next_node.add_child(ident_node)

                self.cursor += 1;

                value:Token = self.stream[self.cursor];
                next_node.add_child(Node(value));

                self.var[ident.value] = True;

            # 变量已声明
            elif root.ttype == TreeType.VAR and ident.value in self.var:
                self.cursor -= 2;
                print("已声明的变量。")
                return;


            #声明函数
            elif root.ttype == TreeType.FUNCTION and ident.value not in self.func:
                root.add_child(ident_node)
                ident_node.add_child(next_node);

                while True:
                    self.cursor += 1;
                    var:Token = self.stream[self.cursor];

                    if var.ttype == TokenType.TK_IDENT:         # ident
                        ident_node.add_child(Node(var));
                    elif var.ttype == TokenType.TK_COMMA:       # ,
                        continue;
                    elif var.ttype == TokenType.TK_CLOSEPA:     # )
                        ident_node.add_child(Node(var));
                        break;
                    else:
                        self.cursor -= 1;
                        self.tree.pop();
                        return;
                
                self.func[ident.value] = True;

                """大括号的内容,以后再写"""
            
            # 函数已声明
            elif root.ttype == TreeType.FUNCTION and ident.value in self.func:
                self.cursor -= 2;
                self.tree.pop();
                print("已声明的函数。");
                return;

            
            self.tree.append(root);


                



        # 调用，赋值
        elif token.ttype == TokenType.TK_IDENT:
            root = RootNode(token);

            self.cursor += 1;
            do:Token = self.stream[self.cursor];
            do_node = Node(do);

            ident_node = Node(token);

            if do.value in ("+","-","++","--","+=","-="):
                pass
            elif do.ttype == TokenType.TK_DOT:        # a.
                pass
            elif do.ttype == TokenType.TK_ASSIGN:   # a = 
                root.ttype = TreeType.ASSIGN;
                root.add_child(do_node);
                do_node.add_child(ident_node);

                self.cursor += 1;
                value:Token = self.stream[self.cursor];
                value_node = Node(value)

                do_node.add_child(value_node);
            elif do.ttype == TokenType.TK_OPENPA:   # a()
                pass
            elif do.ttype == TokenType.TK_OPENBR:   # a[]
                pass
            else:
                pass

            self.tree.append(root);

        
        self.parse();

    


    def print(self):
        for node in self.tree:
            node.print()









            
















