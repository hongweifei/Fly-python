






class Node(object):


    """
    A node in the abstract syntax tree of the program.

    @ivar name: The name of this node.
    @ivar file: The filename where this node comes from.
    @ivar line: The line number of the line on which this node is defined.
    @ivar next: The statement that will execute after this one.
    @ivar statement_start: If present, the first node that makes up the statement that includes this node.
    """


    __slots__ = [
        'name',#node的名字
        'file',#文件名
        'line',#行号
        'next',#在此语句之后执行的语句。
        'statement_start',#如果存在，则为构成包含此节点的语句的第一个节点。
    ];


    def __init__(self,line):
        super().__init__()

        self.filename
        self.line = line
        self.name = None
        self.next = None



