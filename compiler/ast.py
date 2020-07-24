


from .token import *
from enum import Enum,unique,auto


@unique
class TreeType(Enum):

    NONE = auto()       # 

    IMPORT = auto()     # include,import
    RETURN = auto()     # return

    VAR = auto()        # 变量声明
    FUNCTION = auto()   # 函数声明

    UNION = auto()      # 定义联合体
    STRUCT = auto()     # 定义结构体
    CLASS = auto()      # 定义类

    CALL = auto()       # 调用
    ASSIGN = auto()     # 赋值

    IF = auto()         # 如果
    SWITCH = auto()     # 判断
    WHILE = auto()      # while
    FOR = auto()        # for





class Node(object):


    """
    A node in the abstract syntax tree of the program.
    """



    def __init__(self,token = None):
        super().__init__()

        self.token:Token = token;
        self.parent = None;
        self.children = [];

    
    def add_child(self,node):
        if node != None:
            self.children.append(node);
            node.parent = self;


    def get_parent(self):
        return self.parent;


    def get_children(self):
        return self.children;


    def get_parent_num(self) -> int:
        if self.parent == None:
            return 0;
        else:
            n = 0;

            parent:Node = self.parent;
            while parent != None:
                n += 1;
                parent = parent.parent;

            return n;

    
    def print(self):

        if self.parent == None:
            print("--" + self.token.value + "    type:" + str(self.token.ttype))
        else:
            print("--" + "-" * self.get_parent_num() + self.token.value + "    type:" + str(self.token.ttype))


        if self.parent != None and len(self.children) == 0:
            if self is self.parent.children[len(self.parent.children) - 1]:
                print("\n")

        
        for child in self.children:
            child.print()





class RootNode(Node):


    def __init__(self, token = None):
        super().__init__(token = token)
        self.ttype = TreeType.NONE;

    
    def print(self):
        print("Type:" + str(self.ttype));
        return super().print();




        














