"""
实验内容：
请利用区间树实现简易课表管理系统，支持：
1）插入一门新课；
2）删除课程；
3）查询特定时间区间的所有课程名称。注意：每门课信息包括课程编号、课程名称、上课时间。

内容分解：
(done)1. 每棵树的节点信息，课程编号，课程名称，课程时间区间，Max时间，left，right，parent，color
(done)2. 插入一门新课，使用红黑树的插入算法,找到更新max域的地方
(done)3. 删除课程，使用课程编号删除课程
(done)4. 查询与特定时间区间有重合的的节点，输出全部节点
(done)5. 样例部分演示插入，删除，与查询
"""


class IntervalTreeNode():
    course_name = None
    course_number = None
    left = None
    right = None
    parent = None
    key = [0, 0]
    max_time = 0
    color = True  # True 代表红色， False 代表黑色

    def __init__(self, course_name=None, course_number=None, color=True, key=None):
        self.course_number = course_number
        self.course_name = course_name
        self.key = key
        self.color = color  # color为True代表红色，color为False代表黑色


class IntervalTree():
    nil = IntervalTreeNode(color=False)
    root = nil

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
        # 更新max域
        x.max_time = max(x.key[1], x.left.max_time, x.right.max_time)
        y.max_time = max(y.key[1], y.left.max_time, y.right.max_time)

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
        # 更新max域
        x.max_time = max(x.key[1], x.left.max_time, x.right.max_time)
        y.max_time = max(y.key[1], y.left.max_time, y.right.max_time)

    def insert_key(self, key, course_name, course_number):
        z = IntervalTreeNode(key=key, course_name=course_name, course_number=course_number)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key[0] < x.key[0]:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key[0] < y.key[0]:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = True
        # 从下到上更新max域
        w = z
        # w.max_time = max(w.key[1], w.left.max_time, w.right.max_time)
        while w != self.nil:
            if w.max_time == max(w.key[1], w.left.max_time, w.right.max_time):
                break
            w.max_time = max(w.key[1], w.left.max_time, w.right.max_time)
            w = w.parent
        self.insert_fix_up(z)

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

    def delete_course(self, z, course_number):
        if z != self.nil:
            if z.course_number == course_number:
                self.delete_node(z)
            else:
                self.delete_course(z.left, course_number)
                self.delete_course(z.right, course_number)

    def delete_node(self, z):
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
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        # 这里对应z有两个孩子
        if y != z:
            z.key = y.key
            self.update_parent_max_time(z)
        self.update_parent_max_time(y)
        if not y.color:
            self.delete_key_fix_up(x)
        return y

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

    def tree_successor(self, x):
        if x.right != self.nil:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def print_tree(self, z):
        if z != self.nil:
            print("{0} {1} {6}->{2} {3} && {4} {5}".format(z.key, z.color, z.left.key, z.left.color, z.right.key,
                                                           z.right.color, z.max_time))
            self.print_tree(z.left)
            self.print_tree(z.right)

    def update_parent_max_time(self, z):
        w = z
        while w != self.nil:
            if w.max_time == max(w.key[1], w.left.max_time, w.right.max_time):
                break
            w.max_time = max(w.key[1], w.left.max_time, w.right.max_time)
            w = w.parent

    def search_overlap(self, interval, z):
        if z != self.nil:
            if z.key[0] < interval[1] and interval[0] < z.key[1]:
                print("找到一门课程{0} {1}".format(z.course_name, z.course_number))
            self.search_overlap(interval, z.left)
            self.search_overlap(interval, z.right)


if __name__ == "__main__":
    a = IntervalTree()
    a.insert_key([5, 7], "course1", "number1")
    a.insert_key([4, 9], "course2", "number2")
    a.insert_key([7, 8], "course3", "number3")
    a.insert_key([3, 5], "course4", "number4")
    a.insert_key([6, 8], "course5", "number5")
    a.insert_key([8, 10], "course6", "number6")
    a.insert_key([4.5, 7], "course7", "number7")
    a.insert_key([4.2, 5.3], "course8", "number8")
    a.print_tree(a.root)
    print()

    a.search_overlap([6, 6.5], a.root)
    a.delete_course(a.root, "number2")
    print()

    a.search_overlap([6, 6.5], a.root)
    a.print_tree(a.root)
