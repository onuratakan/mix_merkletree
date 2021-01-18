from typing import List
import typing
import hashlib
 
class Node:
    def __init__(self, left, right, value: str,content)-> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.content = content
    
    @staticmethod
    def hash(val: str)-> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()
    def __str__(self):
      return (str(self.value))
 
class MerkleTree:
    def __init__(self, values: List[str])-> None:
        self.__buildTree(values)
 
    def __buildTree(self, values: List[str])-> None:
 
        leaves: List[Node] = [Node(None, None, Node.hash(e),e) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0]) # duplicate last elem if odd number of elements
        self.root: Node = self.__buildTreeRec(leaves) 
    
    def __buildTreeRec(self, nodes: List[Node])-> Node:
        half: int = len(nodes) // 2
 
        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value), nodes[0].content+"+"+nodes[1].content)
        
        left: Node = self.__buildTreeRec(nodes[:half])
        right: Node = self.__buildTreeRec(nodes[half:])
        value: str = Node.hash(left.value + right.value)
        content: str = self.__buildTreeRec(nodes[:half]).content+"+"+self.__buildTreeRec(nodes[half:]).content
        return Node(left, right, value,content)
    
    def printTree(self)-> None:
        self.__printTreeRec(self.root)
 
    def __printTreeRec(self, node)-> None:
        if node != None:
            if node.left != None:
             print("Left: "+str(node.left))
             print("Right: "+str(node.right))
            else:
             print("Input")
            print("Value: "+str(node.value))
            print("Content: "+str(node.content))
            print("")
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)
    
    def getRootHash(self)-> str:
        return self.root.value
        
        
        
def mixmerkletree()-> None:
    elems = ["Mix", "Merkle", "Tree","From","Onur Atakan ULUSOY","https://github.com/onuratakan/mixmerkletree","GO"]
    print("Inputs: ")
    print(*elems, sep = " | ")
    print("")
    mtree = MerkleTree(elems)
    print("Root Hash: "+mtree.getRootHash()+"\n")
    print(mtree.printTree())
 
 
mixmerkletree()
