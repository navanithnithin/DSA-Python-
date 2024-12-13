class TreeNode:
    def __init__(self, data):
        self.data = data
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

    def printTree(self):
        space = " " * self.getLevel() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.printTree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("surface"))
    laptop.addChild(TreeNode("Thinkpad"))

    cellphone = TreeNode(("Cell Phone"))
    cellphone.addChild(TreeNode("Iphone"))
    cellphone.addChild(TreeNode("Google pixel"))
    cellphone.addChild(TreeNode("vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("Samsung"))

    service = TreeNode("Service")

    hardWare = TreeNode("HardWare")
    hardWare.addChild(TreeNode("Tools"))
    hardWare.addChild(TreeNode("Battry"))
    hardWare.addChild(TreeNode("Light"))

    softWare = TreeNode("SoftWare")
    softWare.addChild(TreeNode("Cpu"))
    softWare.addChild(TreeNode("Key Bord"))
    softWare.addChild(TreeNode("Mouse"))

    root.addChild(laptop)
    root.addChild(tv)
    root.addChild(cellphone)
    root.addChild(service)
    service.addChild(hardWare)
    service.addChild(softWare)

    print(hardWare.getLevel())
    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.printTree()
    print(root.getLevel())
