class Node:
    def __init__(self):
        self.countLeaf = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    for ch in s:
        if ch in tmp.child:
            tmp = tmp.child[ch]
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
    tmp.countLeaf += 1

def suffix_traversal(root, level):
    cnt = 1
    for c in root.child:
        cnt += suffix_traversal(root.child[c], level + 1)
    return cnt

def findWord(root, s):
     tmp = root
     for ch in s:
         if ch not in tmp.child:
            return False
         tmp = tmp.child[ch]
      return tmp.countLeaf > 0

def isWord(node):
    return node.countLeaf != 0

def isEmpty(node):
    return len(node.child)

def removeWord(root, s, level, len):
     if root == None:
        return False
     if level == len:
        if root.countLeaf > 0:
            root.countLeaf -= 1
            return True
        return False
     ch = s[level]
     flag = removeWord(root.child[ch], s, level + 1, len)
     if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]) == True:
        tmp = root.child[ch]
        del tmp
        del root.child[ch]
     return flag

if __name__ == '__main__':
     root = Node()
     addWord(root, "the")
     addWord(root, "then")
     addWord(root, "bigo")

     print(findWord(root, "there"))
     print(findWord(root, "th"))
     print(findWord(root, "the"))

     removeWord(root, "bigo", 0, 4)
     removeWord(root, "the", 0, 3)
     removeWord(root, "then", 0, 4)
