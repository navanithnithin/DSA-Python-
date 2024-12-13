class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self, data='both'):
        if data == "name":
            value = self.name
        elif data == "designation":
            value = self.designation
        elif data == "both":
            value = self.name + " ( " + self.designation + " ) "
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.printTree(data)
        # return


def built_managment_tree():
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.addChild(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.addChild(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.addChild(TreeNode("Aamir", "Application Head"))

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.addChild(TreeNode("Peter", "Recruitment Manager"))
    hr_head.addChild(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.addChild(cto)
    ceo.addChild(hr_head)
    cto.addChild(infra_head)
    return ceo


if __name__ == "__main__":
    root_node = built_managment_tree()
    root_node.printTree()
    root_node.printTree("name")
    root_node.printTree("both")
    root_node.printTree("designation")
