#############################################
##########Data Structures Section############
#############################################

class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self, item):
        if len(self.data)==0:
            self.data.append(item)
        else:
            if type(item)==type(self.data[0]):
                self.data.append(item)
            else:
                raise TypeError("Wrong type")
    def dequeue(self):
        if len(self.data)==0:
            raise IndexError("Empty Queue")
        else:
            return self.data.pop(0)
    def length(self):
        return len(self.data)
    def front(self):
        if len(self.data)==0:
            raise IndexError("Empty Queue")
        else:
            return self.data[0]
    def back(self):
        if len(self.data)==0:
            raise IndexError("Empty Queue")
        else:
            return self.data[-1]
class Stack:
    def __init__(self):
        self.data=[]
    def push(self, item):
        if len(self.data)==0:
            self.data.append(item)
        else:
            if type(item)==type(self.data[0]):
                self.data.append(item)
            else:
                raise TypeError("Wrong type")
    def pop(self):
        if len(self.data)==0:
            raise IndexError("Empty Stack")
        else:
            return self.data.pop()
    def length(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def top(self):
        if len(self.data)==0:
            raise IndexError("Empty Stack")
        else:
            return self.data[-1]
class LLNode:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self, head=None):
        if head!=None:
            if(type(head)!=LLNode):
                raise TypeError("Wrong type")
        self.head=head
    def insert(self, data):
        new_node=LLNode(data)
        new_node.next=self.head
        self.head=new_node
    def length(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count
    def search(self, data):
        current=self.head
        found=False
        while current and found is False:
            if current.data==data:
                found=True
            else:
                current=current.next
        if current is None:
            raise ValueError("Data not in list")
        return current
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
    def add_child(self, obj):
        self.children.append(obj)
    def remove_child(self, obj):
        self.children.remove(obj)
class BTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self, root=None):
        if root != None:
            if type(root) != BTreeNode:
                raise TypeError("Wrong type")
        self.root=root    
    def insert(self, data):
        new_node=BTreeNode(data)
        if self.root==None:
            self.root=new_node
        else:
            current=self.root
            parent=None
            while True:
                parent=current
                if data<current.data:
                    current=current.left
                    if current==None:
                        parent.left=new_node
                        return
                else:
                    current=current.right
                    if current==None:
                        parent.right=new_node
                        return
    def inorder(self):
        if self.root:
            self.inorder(self.root.left)
            print(self.root.data)
            self.inorder(self.root.right)
    def preorder(self):
        if self.root:
            print(self.root.data)
            self.preorder(self.root.left)
            self.preorder(self.root.right)
    def postorder(self):
        if self.root:
            self.postorder(self.root.left)
            self.postorder(self.root.right)
            print(self.root.data)
class BST:
    def __init__(self, root=None):
        if root != None:
            if type(root) != BTreeNode:
                raise TypeError("Wrong type")
        self.root=root
    def insert(self, data):
        new_node=BTreeNode(data)
        if self.root==None:
            self.root=new_node
        else:
            current=self.root
            parent=None
            while True:
                parent=current
                if data<current.data:
                    current=current.left
                    if current==None:
                        parent.left=new_node
                        return
                else:
                    current=current.right
                    if current==None:
                        parent.right=new_node
                        return
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
class Trie:
    def __init__(self):
        self.root=[None for _ in range(26)]
        self.is_end=False
    def insert(self, word):
        if len(word==0):
            self.is_end=True
            return
        index=ord(word[0])-ord('a')
        if self.root[index]==None:
            self.root[index]=Trie()
        self.root[index].insert(word[1:])
    def search(self, word):
        if len(word)==0:
            return self.is_end
        index=ord(word[0])-ord('a')
        if self.root[index]==None:
            return False
        return self.root[index].search(word[1:])
    def starts_with(self, prefix):
        if len(prefix)==0:
            return True
        index=ord(prefix[0])-ord('a')
        if self.root[index]==None:
            return False
        return self.root[index].starts_with(prefix[1:])
class Graph:
    def __init__(self, v):
        self.v=v
        self.edges=[[] for _ in range(v)]
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
class Self_Balancing_Tree_Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.direction=1
    def add_child(self, data):
        if self.right!=None and self.left!=None:
            if self.direction==1:
                self.right.add_child(data)
            else:
                self.left.add_child(data)
            self.direction=1-self.direction
        new_node=Self_Balancing_Tree_Node(data)
        if self.direction==1:
            self.right=new_node
        else:
            self.left=new_node
        self.direction=1-self.direction
    def inorder(self):
        if self.left!=None:
            self.inorder(self.left)
        print(self.data)
        if self.right!=None:
            self.inorder(self.right)
    def preorder(self):
        print(self.data)
        if self.left!=None:
            self.preorder(self.left)
        if self.right!=None:
            self.preorder(self.right)
    def postorder(self):
        if self.left!=None:
            self.postorder(self.left)
        if self.right!=None:
            self.postorder(self.right)
        print(self.data)
class MinHeap:
    def __init__(self, arr):
        self.heap=arr
        self.heap_size=len(arr)
        self.build_min_heap()
    def build_min_heap(self):
        for i in range(self.heap_size//2, -1, -1):
            self.min_heapify(i)
    def min_heapify(self, i):
        l=2*i+1
        r=2*i+2
        smallest=i
        if l<self.heap_size and self.heap[l]<self.heap[smallest]:
            smallest=l
        if r<self.heap_size and self.heap[r]<self.heap[smallest]:
            smallest=r
        if smallest!=i:
            self.heap[i], self.heap[smallest]=self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
    def extract_min(self):
        if self.heap_size==0:
            raise IndexError("Heap is empty")
        min=self.heap[0]
        self.heap[0]=self.heap[self.heap_size-1]
        self.heap_size-=1
        self.min_heapify(0)
        return min
    def decrease_key(self, i, key):
        if key>self.heap[i]:
            raise ValueError("New key is greater than current key")
        self.heap[i]=key
        while i>0 and self.heap[i//2]>self.heap[i]:
            self.heap[i], self.heap[i//2]=self.heap[i//2], self.heap[i]
            i=i//2
    def insert(self, key):
        self.heap_size+=1
        self.heap.append(float("inf"))
        self.decrease_key(self.heap_size-1, key)
    def delete(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()
class MaxHeap:
    def __init__(self, arr):
        self.heap=arr
        self.heap_size=len(arr)
        self.build_max_heap()
    def build_max_heap(self):
        for i in range(self.heap_size//2, -1, -1):
            self.max_heapify(i)
    def max_heapify(self, i):
        l=2*i+1
        r=2*i+2
        largest=i
        if l<self.heap_size and self.heap[l]>self.heap[largest]:
            largest=l
        if r<self.heap_size and self.heap[r]>self.heap[largest]:
            largest=r
        if largest!=i:
            self.heap[i], self.heap[largest]=self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    def extract_max(self):
        if self.heap_size==0:
            raise IndexError("Heap is empty")
        max=self.heap[0]
        self.heap[0]=self.heap[self.heap_size-1]
        self.heap_size-=1
        self.max_heapify(0)
        return max
    def increase_key(self, i, key):
        if key<self.heap[i]:
            raise ValueError("New key is smaller than current key")
        self.heap[i]=key
        while i>0 and self.heap[i//2]<self.heap[i]:
            self.heap[i], self.heap[i//2]=self.heap[i//2], self.heap[i]
            i=i//2
    def insert(self, key):
        self.heap_size+=1
        self.heap.append(float("-inf"))
        self.increase_key(self.heap_size-1, key)
    def delete(self, i):
        self.increase_key(i, float("inf"))
        self.extract_max()

#############################################
###############Algos Section#################
#############################################

def binary_search(arr, data):
    if arr==None or data==None or type(arr)!=list or type(data)!=int:
        raise TypeError("Wrong type")
    if len(arr)==0:
        return False
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==data:
            return True
        elif arr[mid]<data:
            l=mid+1
        else:
            r=mid-1
    return False
def binary_search_index(arr, data):
    if arr==None or data==None or type(arr)!=list or type(data)!=int:
        raise TypeError("Wrong type")
    if len(arr)==0:
        return -1
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==data:
            return mid
        elif arr[mid]<data:
            l=mid+1
        else:
            r=mid-1
    return -1
def DFS_helper(g, i, visited):
    visited[i]=True
    print(i)
    for j in g.edges[i]:
        if visited[j]==False:
            DFS_helper(g, j, visited)
def DFS(g):
    if type(g)!=Graph:
        raise TypeError("Wrong type")
    visited=[False for _ in range(g.v)]
    for i in range(g.v):
        if visited[i]==False:
            DFS_helper(g, i, visited)
def BFS(g):
    if type(g)!=Graph:
        raise TypeError("Wrong type")
    visited=[False for _ in range(g.v)]
    queue=[]
    for i in range(g.v):
        if visited[i]==False:
            queue.append(i)
            visited[i]=True
            while len(queue)!=0:
                node=queue.pop(0)
                print(node)
                for j in g.edges[node]:
                    if visited[j]==False:
                        queue.append(j)
                        visited[j]=True
def Tree_search(root, data):
    if data==None or root==None or type(data)!=type(root.data) or type(root)!=TreeNode:
        raise TypeError("Wrong type")
    if root.data==data:
        return True
    if root.left!=None:
        if Tree_search(root.left, data):
            return True
    if root.right!=None:
        if Tree_search(root.right, data):
            return True
    return False
def BTree_Search(root, data):
    if data==None or root==None or type(data)!=type(root.data) or type(root)!=BTreeNode:
        raise TypeError("Wrong type")
    if root.data==data:
        return True
    if root.left!=None:
        if BTree_Search(root.left, data):
            return True
    if root.right!=None:
        if BTree_Search(root.right, data):
            return True
    return False
def BST_Search(root, data):
    if data==None or root==None or type(data)!=type(root.data) or type(root)!=BTreeNode:
        raise TypeError("Wrong type")
    if root.data==data:
        return True
    if root.data>data:
        if root.left!=None:
            return BST_Search(root.left, data)
    else:
        if root.right!=None:
            return BST_Search(root.right, data)
    return False
def next_greater_element(arr):
    if arr==None or type(arr)!=list:
        raise TypeError("Wrong type")
    n=len(arr)
    s=Stack()
    s.push(0)
    for i in range(1, n):
        while not s.is_empty() and arr[s.top()]<arr[i]:
            print(arr[i])
            s.pop()
        s.push(i)
    while not s.is_empty():
        print(-1)
        s.pop()
def next_smaller_element(arr):
    if arr==None or type(arr)!=list:
        raise TypeError("Wrong type")
    n=len(arr)
    s=Stack()
    s.push(0)
    for i in range(1, n):
        while not s.is_empty() and arr[s.top()]>arr[i]:
            print(arr[i])
            s.pop()
        s.push(i)
    while not s.is_empty():
        print(-1)
        s.pop()
def kadanes_algo(arr):
    if arr==None or type(arr)!=list:
        raise TypeError("Wrong type")
    n=len(arr)
    max_ending_here=0
    max_so_far=0
    for i in range(n):
        max_ending_here+=arr[i]
        if max_ending_here<0:
            max_ending_here=0
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
    return max_so_far
def max_product_subarray(arr):
    if arr==None or type(arr)!=list:
        raise TypeError("Wrong type")
    n=len(arr)
    max_ending_here=1
    min_ending_here=1
    max_so_far=1
    for i in range(n):
        if arr[i]>0:
            max_ending_here*=arr[i]
            min_ending_here=min(1, min_ending_here*arr[i])
        elif arr[i]==0:
            max_ending_here=1
            min_ending_here=1
        else:
            temp=max_ending_here
            max_ending_here=max(1, min_ending_here*arr[i])
            min_ending_here=temp*arr[i]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
    return max_so_far

#####################END#####################