class RBNode():
    left = None
    right = None
    parent = None
    key = 0
    color = True  # True 代表红色， False 代表黑色

    def __init__(self, key=None, color=True, parent=None, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color  # color为True代表红色，color为False代表黑色
        self.key = key


# 测试在使用类似x = x.left 的时候是否改变了什么东西，测试完成，没有改变ID
class RBTree():
    nil = RBNode(color=False)
    root = nil

    # 左旋函数测试通过
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    # 右旋函数测试通过
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # 普通插入测试通过
    def insert_key(self, key):
        z = RBNode(key=key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = True
        self.insert_fix_up(z)

    # 测试通过
    def insert_fix_up(self, z):
        while z.parent.color:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = False  # 确定这两句话应该处于的位置
                    z.parent.parent.color = True  # 确定这句话的缩进
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = False  # 确定这句话的缩进
                    z.parent.parent.color = True  # 确定这句话的缩进
                    self.left_rotate(z.parent.parent)
        self.root.color = False

    # 删除函数得到验证
    def delete_key(self, z):
        # y是要删除的节点，这个if循环找到要删除的节点
        if z.left == self.nil or z.right == self.nil:
            y = z
        else:
            y = self.tree_successor(z)

        if y.left != self.nil:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key
        if not y.color:
            self.delete_key_fix_up(x)
        return y

    # 完成测试
    def delete_key_fix_up(self, x):
        while x != self.root and not x.color:
            if x == x.parent.left:
                w = x.parent.right
                if w.color:
                    w.color = False
                    x.parent.color = True
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if not w.left.color and not w.right.color:
                    w.color = True
                    x = x.parent
                else:
                    if not w.right.color:
                        w.left.color = False
                        w.color = True
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color:
                    w.color = False
                    x.parent.color = False
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if not w.right.color and not w.left.color:
                    w.color = True
                    x = x.parent
                else:
                    if not w.left.color:
                        w.right.color = False
                        w.color = True
                        self.left_rotate(w)
                        w = x.parent.left
                        w.color = x.parent.color
                    x.parent.color = False
                    w.left.color = False
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = False

    # 通过测试
    def tree_successor(self, x):
        if x.right != self.nil:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    # 完成测试
    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    # 按照层次打印数的结构
    def print_tree(self, z):
        if z != self.nil:
            print("{0} {1}->{2} {3} && {4} {5}".format(z.key, z.color, z.left.key, z.left.color, z.right.key,
                                                       z.right.color))
            self.print_tree(z.left)
            self.print_tree(z.right)


if __name__ == "__main__":
    a = RBTree()
    # 12 1 9 2 0 11 7 19 4 15 18 5 14 13 10 16 6 3 8 17
    a.insert_key(12)
    a.insert_key(1)
    a.insert_key(9)
    a.insert_key(2)
    a.insert_key(0)
    a.insert_key(11)
    a.insert_key(7)
    a.insert_key(19)
    a.insert_key(4)
    a.insert_key(15)
    a.insert_key(18)
    a.insert_key(5)
    a.insert_key(14)
    a.insert_key(13)
    a.insert_key(10)
    a.insert_key(16)
    a.insert_key(6)
    a.insert_key(3)
    a.insert_key(8)
    a.insert_key(17)
    a.print_tree(a.root)