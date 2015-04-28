class RBNode():
    left = None
    right = None
    parent = None
    key = 0
    color = True

    def __init__(self, key=None, color=True, parent=None, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color  # color为True代表红色，color为False代表黑色
        self.key = key


class RBTree():
    nil = RBNode(color=False)
    root = nil

    def __init__(self):
        print("初始化建树")

    # todo 测试左旋函数，构造测试样例
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

    # todo 测试右旋函数，构造测试样例
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

    def insert_fix_up(self, z):
        while z.parent.color:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = False
                z.parent.parent.color = True
                self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color:
                    z.parent.color = False
                    y.color = False
                    z.parent.parent.color = True
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = False
                z.parent.parent.color = True
                self.left_rotate(z.parent.parent)
        self.root.color = False

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

    # todo 测试函数正确性
    def delete_key(self, z):
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
            # todo 拷贝数据
        if not y.color:
            self.delete_key_fix_up(x)
        return y

    def prints(self, z):
        if z != self.nil:
            # return str(self.printTree(z.left)) + " " + str(z.key) + " " + str(self.printTree(z.right))
            self.prints(z.left)
            print(str(z.key) + " " + str(z.color), end=" ")
            self.prints(z.right)

    def tree_successor(self, x):
        if x.right != self.nil:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.parent:
            x = y
            y = y.parent
        return y

    def delete_key_fix_up(self, x):
        while x != self.root and not x.color:
            if x == x.parent.left:
                w = x.parent.right
                if w.color:
                    w.color = False
                    x.parent.color = False
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if not w.left.color and not w.right.color:
                    w.color = True
                    x = x.parent
                elif not w.right.color:
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
                elif not w.left.color:
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

    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x


if __name__ == "__main__":
    a = RBTree()
    a.insert_key(12)
    a.insert_key(11)
    a.insert_key(10)
    a.insert_key(13)
    a.insert_key(14)
    a.insert_key(15)
    a.insert_key(3)
    a.prints(a.root)