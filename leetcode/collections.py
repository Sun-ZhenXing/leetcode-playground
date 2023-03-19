# ----------------------------------------
# 为 leetcode.com/leetcode.cn 设计的工具包
# 包含自动输入输出工具包
# ----------------------------------------


import inspect
from collections import Counter, OrderedDict, defaultdict, deque
from types import FunctionType, MethodType
from typing import (Any, List, Iterable, Iterator, Optional, Union, get_args,
                    get_origin)

__all__ = [
    'NestedInteger',
    'Counter',
    'OrderedDict',
    'defaultdict',
    'deque',
    'List',
    'null',
    'Iterable',
    'Iterator',
    'Optional',
    'Union',
    'Any',
    'ListNode',
    'Node',
    'TreeNode',
    'make_tree',
    'make_binary_tree',
    'make_linked_list',
    'any_praser',
    'debug',
    'print_debug'
]
__author__ = 'Alex Sun: sun-zhenxing@github.com'
__version__ = (0, 1)

# NULL 定义
null = None

# 默认的树打印缩进
DEFAULT_SPACE = '  '


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self.value = None
            self.list = []
        else:
            self.list = None
            self.value = value

    def __repr__(self) -> str:
        return 'L<{} {}>'.format(self.value, self.list)

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.value is not None and self.list is None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self.list is None:
            self.list = [elem]
        else:
            self.list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.list


class ListNode:
    '''
    单链表结点
    '''

    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        # 检查是否存在环，如果存在则报错
        ring = self.exist_ring(self)
        if ring is not None:
            raise ValueError("linked list has ring at "
                             "'{}'".format(ring.val))

        # 表示为
        # List[1 -> 2 -> 3 -> 4]
        res = 'List[{}'.format(self.val)
        curr = self.next
        while curr:
            res += ' -> {}'.format(curr.val)
            curr = curr.next
        res += ']'
        return res

    @staticmethod
    def exist_ring(node: 'ListNode') -> 'ListNode':
        '''
        检查链表内是否包含环,
        如果有环则返回环的入口结点, 否则返回 `None`
        '''
        if node is None or node.next is None:
            return None
        # 快慢指针法快速判断
        slow = node
        quick = node.next
        while slow != quick:
            if quick is None or quick.next is None:
                return None
            slow = slow.next
            quick = quick.next.next
        return slow


class Node:
    '''
    N 叉树结点
    '''

    def __init__(self, val: int = None,
                 children: Iterable['Node'] = None):
        self.val = val
        if children is not None:
            self.children = list(children)
        else:
            self.children = list[Node]()

    def __repr__(self) -> str:
        return 'Tree:\n' + self._my_repr_()

    def _my_repr_(self, recu: int = 0) -> str:
        res = '{}- {}'.format(DEFAULT_SPACE * recu, self.val)
        for node in self.children:
            if isinstance(node, Node):
                res += '\n' + node._my_repr_(recu + 1)
            else:
                res += '\n{}- ~'.format(
                    DEFAULT_SPACE * (recu + 1)
                )
        return res


class TreeNode:
    '''
    二叉树节点
    '''

    def __init__(self, val=0, left: 'TreeNode' = None,
                 right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return 'Binary Tree:\n' + self._my_repr_()

    def _my_repr_(self, recu: int = 0) -> str:
        res = '{}- {}'.format(DEFAULT_SPACE * recu, self.val)

        # 这可以区分是左子树还是右子树
        # 默认是左子树，出现空行则是右子树
        if self.left is None and self.right is not None:
            res += '\n{}- ~'.format(
                DEFAULT_SPACE * (recu + 1)
            )
        if isinstance(self.left, TreeNode):
            res += '\n' + self.left._my_repr_(recu + 1)
        if isinstance(self.right, TreeNode):
            res += '\n' + self.right._my_repr_(recu + 1)
        return res


def make_tree(__iterable: Iterable[int]) -> 'Node':
    '''
    通过层序遍历生成 N 叉树
    @param `__iterable` 构造 N 叉树的层序遍历
    '''
    queue = deque[Node]()
    head = Node(None, [])
    queue.append(head)
    for val in __iterable:
        if val is not None:
            node = Node(val)
            queue.append(node)
            if queue[0].children:
                queue[0].children.append(node)
            else:
                queue[0].children = [node]
        else:
            queue.popleft()
    return head.children[0]


def make_binary_tree(__iterable: Iterable[int]) -> TreeNode:
    '''
    通过层序遍历生成二叉树
    @param `__iterable` 构造二叉树的层序遍历
    '''
    arr = list(__iterable)
    if not arr:
        return None
    queue = deque[TreeNode]()
    head = TreeNode(arr[0])
    queue.append(head)
    i = 1
    while queue:
        cur = queue.popleft()
        if i < len(arr):
            if arr[i] is not None:
                cur.left = TreeNode(arr[i])
                queue.append(cur.left)
            i += 1
        if i < len(arr):
            if arr[i] is not None:
                cur.right = TreeNode(arr[i])
                queue.append(cur.right)
            i += 1
    return head


def make_linked_list(__iterable: Iterable[int]) -> 'ListNode':
    '''
    通过列表生成链表, 不包含头结点
    @param arr 列表
    '''
    head = ListNode()
    node = head
    for val in __iterable:
        node.next = ListNode(val)
        node = node.next
    return head.next


def any_praser(expr: str, typeof: type) -> Any:
    '''
    表达式解析器
    @param `expr` 被解析的表达式
    @param `typeof` 被解析的类型

    `Optional` 类型是受支持的

    ### 注意

    此函数使用 `eval` 函数解析输入, 这在多数场合下是 **不安全的**
    '''
    if typeof is Any:
        return eval(expr)
    # 支持 Optional 类型
    if get_origin(typeof) is Union:
        t1, t2 = get_args(Optional[str])
        if t2 is type(None):
            arg = t1
        else:
            arg = t2
        return any_praser(expr, arg)
    if typeof is ListNode:
        return make_linked_list(eval(expr))
    if typeof is TreeNode:
        return make_binary_tree(eval(expr))
    if typeof is Node:
        return make_tree(eval(expr))
    return eval(expr)


def debug(func: Union[MethodType, FunctionType]) -> Any:
    '''
    调试指定函数或方法, 函数或方法要使用类型注解全部参数

    如果传入的是类或类的实例, 那么将自动查找一个函数进行调试
    '''

    # 如果是类
    if type(func) is type:
        cls_ = func
        instance = func()

    # 如果是类的实例
    elif type(func) is not MethodType and\
            type(func) is not FunctionType:
        cls_ = type(func)
        instance = func
    else:
        cls_ = None

    if cls_ is not None:
        method_list = [
            name
            for name in dir(cls_)
            if inspect.isfunction(getattr(cls_, name))
        ]
        if len(method_list) == 0:
            print('没有函数可供调试')
            return None
        if len(method_list) == 1:
            name = method_list.pop()
            print("'{}' 将被调试...".format(name))
            # 此时函数被丢弃，需要实例的方法
            # 原因是 Python 的将类的成员视为函数，只有类的实例才是方法
            # 必须反射实例的方法才能正常工作
            return debug(getattr(instance, name))
        else:
            print('有 {} 个函数在此类中, 请指定要调试的函数'.format(len(method_list)))
            for i, name in enumerate(method_list):
                print('{}. {}'.format(i + 1, name))
            index = int(input('请输入序号 > '))
            return debug(getattr(instance, method_list[index - 1]))

    sig = inspect.signature(func)
    params = sig.parameters
    param_list = []
    for param in params:
        annotation = params[param].annotation
        if isinstance(annotation, str):
            annotation = eval(annotation)
        # 如果没有类型注解，则是 Any
        if annotation is inspect._empty:
            annotation = Any
        # 如果是容器类型，则是 Any
        if get_origin(annotation) in {
            dict, list, tuple, set, frozenset
        }:
            annotation = Any
        if annotation not in INPUT_TIP:
            annotation = Any
        expr = input(INPUT_TIP[annotation].format(param))
        if expr == '':
            expr = 'None'
        param_list.append(any_praser(expr, annotation))
    return func(*param_list)


def print_debug(func: Union[MethodType, FunctionType]) -> None:
    '''
    相当于 `print(debug(func))`
    对指定函数进行调试输出
    '''
    print(debug(func))


INPUT_TIP = {
    Any: '{}: any type > ',
    bool: '{}: bool > ',
    bytearray: '{}: bytearray > ',
    bytes: '{}: bytes > ',
    complex: '{}: complex > ',
    dict: '{}: dict > ',
    float: '{}: float > ',
    frozenset: '{}: frozenset > ',
    int: '{}: int > ',
    list: '{}: list > ',
    object: '{}: object > ',
    range: '{}: range > ',
    set: '{}: set > ',
    str: '{}: str > ',
    tuple: '{}: tuple > ',
    ListNode: '{}: linked list > ',
    Node: '{}: n-tree node > ',
    TreeNode: '{}: binary tree node > '
}

assert TreeNode in INPUT_TIP

if __name__ == '__main__':
    print(make_tree([1, null, 3, 2, 4, null, 0, 6]))
    print(make_binary_tree([1, 2, 3, null, 4, 5, 6]))
