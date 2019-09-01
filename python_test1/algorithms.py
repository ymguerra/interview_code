# input: {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# output:  {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
from time import time

def group_by_owners(files):
    output = {}
    for i in files: 
        if files[i] not in output:
            output.update({files[i]: [ item for item in files.keys() if files[item] == files[i] ]})
    
    return output
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))
print ('*********************** group_by_owners **************************************')

def is_palindrome(word):
    return word.lower() == word[::-1].lower()   
    
print(is_palindrome('Deleveled'))
print ('*********************** palindrome **************************************')

import collections
import csv

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        temp_path = []
        result = []
        if new_path.startswith('/'):
            temp_path = new_path.split('/')
        else:
            temp_path = self.current_path.split('/') + new_path.split('/')
       
        for item in temp_path:
            if item == '..':
                result.pop()
            elif item == '':
                continue
            else:
                result.append(item)
            
        self.current_path = '/' + '/'.join(result)

path = Path('/a/b')
path.cd('../x')
print(path.current_path)
print ('*********************** cd Path **************************************')
"""
class Path:
    def __init__(self, path):
        self._internal_path = []
        self.cd(path)

    def cd(self, new_path):
        if not new_path.startswith('/'): #is relative
            self._internal_path += self._split(new_path)
        else:
            self._internal_path = self._split(new_path)
        
        self._compress()
     
    def _split(self, path):
        return path.split('/')
    
    def _compress(self):
        temp = []
        for elm in self._internal_path:

            if elm == '..':
                temp and temp.pop()
            elif elm == '':
                continue
            else:
                temp.append(elm)
        self._internal_path = temp
    
    @property
    def current_path(self):
        return '/' + '/'.join(self._internal_path)


path = Path('/a/b/c/d')
path.cd('../../x/m/kjk/fghgh')
print(path.current_path)

"""
#import random as random

#print ("qyzqwe".center(7,'1'))

#print (sum(map(lambda x: x*2, range(1,11))))

#print ('new' 'line')
#print (" deaf {x1} and {x2}".format(x1='abc', x2='dfg'))

i = 5
while True:
    if i%11 == 0:
        break
    print (i)
    i +=1

#print ("xyz. QWE".capitalize())

"""
    cant = input()
    str_array = input()
    str_array = str_array.split()
    even = sum([int(x) for x in str_array if int(x)%2 == 0])
    odd = sum([int(x) for x in str_array if int(x)%2 != 0])
    #result = sorted(map(int, str_array.split()), reverse=True)
    if even > odd:
        print('Even', end='')
    elif odd > even:
        print('Odd', end='')
    else:
        print('Tied', end='')

#******************************************

import collections

cant = input()
str_array = input()
str_array = str_array.split()
counter = dict(collections.Counter([int(x) for x in str_array]))

print(list(counter.keys())[0], end='')
#******************************************

cant = input()
str_array = input()
#str_array = str_array.split()
result = [int(x) for x in str_array.split()]
print (max(result) - min(result), end='')

#******************************************

cant = input()
str_array = input()
str_array = str_array.split()
even = [x for x in str_array if int(x)%2 == 0]

if even:
    print(''.join(even), end='')
else:
    print('0', end='')
"""


def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(staircase(4))
print ('**************** stair case *********************************')

def add_up_to(k, list_param):    
    for pos in range(0,len(list_param) -1):
        element = list_param[pos]
        for pos2 in range(pos+1, len(list_param)):
            if element + list_param[pos2] == k:
                return True
    return False

def add_up_to_two(k, list_param):    
    for val in list_param:
        if k - val in list_param:
            return True
        
    return False

print(add_up_to_two(13, [10, 15, 3, 7]))
print ('**************** add_up_to *********************************')

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_memoized(n, cache):
    if cache[n] != None:
        return cache[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memoized(n-1,cache) + fib_memoized(n-2,cache)
    cache[n] = result    
    return result

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    buttom_up = [0 for _ in range(n+1)]
    buttom_up[1] = 1
    buttom_up[2] = 1
    for i in range(3,n+1):
        buttom_up[i] = buttom_up[i-1] + buttom_up[i-2]
    
    return buttom_up[n]


n= 10
#memoized = [None for _ in range(n+1)]
#print (fib_memoized(n,memoized))
#print(fib(n))

print (fib_bottom_up(n))
print ('**************** fib *********************************')

import heapq
"""
    lists: [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    devuelve una sola lista ordenada
"""
def marge(lists):
    marged_lists = []
    print (list(enumerate(lists)))

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        marged_lists.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind +1)
            heapq.heappush(heap, next_tuple)

    return marged_lists

#print (marge([[10, 15, 30], [12, 15, 20], [8, 17, 32]]))
print ('*********************** heap marge **************************************')

def array_products(lists):
    result = []

    i = 0
    while i < len(lists):
        value_pos = 1
        for pos, val in enumerate(lists):
            if pos != i:
                value_pos *= val               

        result.append(value_pos)
        i += 1

    return result

print (array_products([2, 10]))
initial_time = time()
print (array_products([1, 2, 3, 4, 5]))
end_time = time()
print (f'the time was: {end_time - initial_time}')
#print (array_products([3, 2, 1]))

def array_products_two(lists):
    result = []
    
   # if lists and min(lists) == 0:
   #     return [0]
      
    multip = 1
    for i in lists:
        multip *= i
        if multip == 0:
            return [0]
    
    for i in lists:
        result.append(int(multip/i))

    return result

print (array_products_two([10, 3, 5, 6, 2] ))
initial_time = time()
print (array_products_two([1, 2, 3, 4, 5]))
end_time = time()
print (f'the time was: {end_time - initial_time}')
print (array_products_two([3, 2, 1]))

print ('************************** array_products ***********************************')
"""
    Serializar y deserializar un arbol
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self,sentinel='#'):
        if self.left == None and self.right == None:
            return f'{self.val}-*N-*N'

        elif self.left == None:
            return f'{self.val}-*N-*{self.right.serialize()}'
        
        elif self.right == None:
            return f'{self.val}-*{self.left.serialize()}-*N'
        
        else:
            return f'{self.val}-*{self.left.serialize()}-*{self.right.serialize()}'
    
    def serialize2(self, sentinel='#'):
        serial = [self.val]
        if self.left is None:
            serial.append(sentinel)
        else:
            serial.extend(self.left.serialize2(sentinel))
        if self.right is None:
            serial.append(sentinel)
        else:
            serial.extend(self.right.serialize2(sentinel))
        return serial
  
    @classmethod
    def deserialize(cls, source, sentinel='#'):
        def _helper(index):
            if source[index] == sentinel:
                return None, index + 1

            value = source[index]
            left, index = _helper(index + 1)
            right, index = _helper(index)
            return cls(value, left, right), index

        aux = _helper(0)
        return aux[0]

def deserialize(str_node):    
    return  Node.deserialize(str_node.split('*-'))
    
def serialize(node):
    return '*-'.join(node.serialize2())

node = Node('root', Node('left', Node('left.left')),Node('right'))
node2 = Node('nochild')

#print (serialize(node))
#print (serialize(node2))
#print (deserialize(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print ('********************** serialize deserialize tree ***************************************')
'''
    Given an array of integers, find the first missing positive integer in linear time and constant space. 
    In other words, find the lowest positive integer that does not exist in the array. 
    The array can contain duplicates and negative numbers as well.
'''
def missing_positive_integer(input_list):
    input_list.sort()
    result = 0
    if len(input_list) == 1 and input_list[0] >= 0:
        return input_list[0] + 1

    for pos in range (0, len(input_list)):
        if input_list[pos] < 0:
            continue
        elif pos + 1 == len(input_list) or input_list[pos] + 1 < input_list[pos+1]:
            result = input_list[pos] + 1
            break

    return result

print (missing_positive_integer([3, 4, -1, 1]))
print (missing_positive_integer([-2, -1, 5, 0]))
print (missing_positive_integer([1, 2, 0]))
print (missing_positive_integer([0]))
print (missing_positive_integer([]))
print (missing_positive_integer([1, -1, -5, -3, 3, 4, 2, 8]))

print ('********************** missing_positive_integer **********************************')

'''
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
     For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
'''
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def first(a, b):
        return a
    return f(first)

def cdr (f):
    def last(a, b):
        return b
    return f(last)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
print ('********************** first and last element of that pair **********************************')

# [1, 2, 3, 4] -> [1, 2, 3, 5]

def sum_one_to_array(input_array):
    pass

'''
    Given mapping a=1, b=2, ..., z=26 and encoded message, count the number of ways
    it can be decoded

    '111' ---> 3 ('aaa', 'ka', 'ak')

'''
def decode_message_memo(encode_message, n, memo):
    '''
        encode_message: string with only number '1111'
                     n: array length, it will be decreasing in every iteration
                  memo: array with all the saving states
    '''
    if n == 0:    #base case
        return 1        
    
    s = len(encode_message) - n
    if encode_message[s] == '0':  #base case
        return 0

    if memo[n] != None:  # getting values from memory
        return memo[n]
    
    result = decode_message_memo(encode_message, n-1, memo)
    if n >= 2 and int(encode_message[s:s+2]) <= 26:   # if two consecutive numbers are less than 26
        result += decode_message_memo(encode_message, n-2, memo)
    
    memo[n] = result  # saving results in memory

    return result

message = '12611'
memo = [None for _ in range(len(message) + 1)]

print(decode_message_memo(message, len(message), memo))
print ('********************** decode message **********************************')

'''
    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
    Given the root to a binary tree, count the number of unival subtrees.

                         0
                        / \
                        1   0     ------> 5
                            / \
                           1   0
                          / \
                         1   1
'''
class BTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unival_subtrees_count(tree):
    if not tree.left and not tree.right:
        return 1
    
    count = 0
    if tree.left and tree.right and tree.left.val == tree.val and tree.right.val == tree.val:
        count += unival_subtrees_count(tree.left) + unival_subtrees_count(tree.right) + 1
    
    elif tree.left and not tree.right and tree.left.val == tree.val:
        count += unival_subtrees_count(tree.left) + 1
        
    elif tree.right and not tree.left and tree.right.val == tree.val:
        count += unival_subtrees_count(tree.right) + 1
    
    elif tree.left and tree.right:
        count += unival_subtrees_count(tree.left) + unival_subtrees_count(tree.right)
    
    elif tree.left and not tree.right:
        count += unival_subtrees_count(tree.left)
    
    elif tree.right and not tree.left:
        count += unival_subtrees_count(tree.right)

    return count

def count(node):
  return count(node.left) + count(node.right) + 1 if node else 0
  
def deepest(node):
    if node and not node.left and not node.right:
        return (node, 1) # Leaf and its depth

    if not node.left: # Then the deepest node is on the right subtree
        return increment_depth(deepest(node.right))
    elif not node.right: # Then the deepest node is on the left subtree
        return increment_depth(deepest(node.left))

    return increment_depth(
            max(deepest(node.left), deepest(node.right),
                    key=lambda x: x[1])) # Pick higher depth tuple and then increment its depth

def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return (node, depth + 1)    


my_tree = BTree(0, BTree(1), BTree(0, BTree(1, BTree(1), BTree(1)), BTree(0)))

tree = BTree(1)
print (count(my_tree))

print (unival_subtrees_count(my_tree))
print ('********************** unival tree count **********************************')

'''
    Given a list of integers, write a function that returns the largest
    sum of non-adjacent numbers. Numbers can be 0 o negative

    [2, 4, 6, 2, 5] ---> 13 since we pick 2, 6 and 5
    [5, 1, 1, 5]    ---> 10 since we pick 5 and 5
'''
def largest_sum_of_non_adjacent(given_array, n):
    if n <= 0:
        return 0
    
    pos = len(given_array) - n
    result1, result2 = (0,0)

    result1 += given_array[pos] + largest_sum_of_non_adjacent(given_array, n-2)
    
    if pos + 1 < len(given_array):
        result2 += given_array[pos+ 1] + largest_sum_of_non_adjacent(given_array, n-3)

    if result1 > result2:
        return result1
    else:
        return result2

def find_max_sum(arr, n):
    incl = 0
    excl = 0

    for i in arr:
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return (excl if excl > incl else incl)

print(largest_sum_of_non_adjacent([2, 4, 6, 2, 5], 5))
print(largest_sum_of_non_adjacent([5, 1, 1, 5], 4))
print(largest_sum_of_non_adjacent([5, 5, 10, 100, 10, 5], 6))
print(largest_sum_of_non_adjacent([1, 2, 3], 3))
print(largest_sum_of_non_adjacent([1, 20, 3], 3))

print(find_max_sum([5, 5, 10, 100, 10, 5], 6))
print(find_max_sum([1, 2, 3], 3))
print(find_max_sum([1, 20, 3], 3))
print ('********************** largest sum og non-adjacent numbers **********************************')

'''
    Implement a job schudler which takes in a function f
    and an integer n, and calls f after n milliseconds
'''

from time import sleep

def job_schudler_2(func, n):
    sleep(n / 1000)
    func()

def job_schudler(func, n):
    now = time()
    while True:
        untill = time()
        if untill - now >= n/1000:
            func()
            break

def sample_funtion():
    print('Hello')

job_schudler_2(sample_funtion, 1000)
print ('********************** job schudler **********************************')

'''
    Implement an autocomplete system. That is, given a query string s and a set of all
    possible query strings, return all strings in the set that have s as a prefix.

    ['dog', 'deer', 'deal'] --- searching for 'de' return ['deer', 'deal']
'''
class TreeNode():
    def __init__(self):
        self.children = []
        self.is_end = True
        self.word = ''

    def find_letter(self, letter):
        for l, _ in self.children:
            if l == letter:
                return True        
        return False

    def add_letter(self, letter):
        self.children.append((letter, TreeNode()))
        self.is_end = False
    
    def get_node_by_letter(self, letter):
        for l, node in self.children:
            if l == letter:
                return (l, node)        
        return None

class WordTree():
    def __init__(self):
        self.root = TreeNode()        

    def insert(self, word):
        node = self.root
        for i in word:
            if not node.find_letter(i):
                node.add_letter(i)    

            _, node = node.get_node_by_letter(i)
        node.is_end = True
        node.word = word
    
    def search(self, word):
        aux_word = ''
        node = self.root
        if node.is_end:
            return [node.word]

        for ch in word:
            if node.find_letter(ch):
                l, node = node.get_node_by_letter(ch)
                aux_word += l
        
        if len(aux_word) != len(word):
            return []
        else:
            return self._search_rest_of_word(node)


    def _search_rest_of_word(self, node):
        result = []
        if node.is_end:
            return [node.word]
        
        for _, node in node.children:
            result.extend(self._search_rest_of_word(node))
            
        return result

wordTree = WordTree()
wordTree.insert('dog')
wordTree.insert('deer')
wordTree.insert('deal')
print (wordTree.search('de'))

print ('********************** tree word search **********************************')

'''
Uniformly picking a random element from a gigantic stream
'''

import random

def pick_element(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i+1) == 1:
            random_element = e
        
    return random_element

print ('***************** Uniformly picking a random element ********************************')

'''
    Pick itinerary
    Given an unordered list of flights taken by someone each represented as (Orig - Desti)
    pairs and a starting airport, compute the person's itinerary.  If no such itinerary exist
    return null. All flights must be used in the itinerary for example
    
        HNL - AKL     Starting at YUL
        YUL - ORD     Result -> YUL - ORD - SFO - YNL - AKL
        ORD - SFO
        SFO - HNL
'''
def get_itinerary(flights, current_itinerary):
    if not flights:
        return current_itinerary
    
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        flights_minus_current = flights[:i] + flights[i+1:]
        current_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        
        current_itinerary.pop()
    
    return None


print(get_itinerary([('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD','SFO'), ('SFO', 'HNL')], ['YUL']))
print ('***************** Pick itinerary ********************************')

'''
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
'''
def estimate_pi(interval):
    circle_points, square_points = 0, 0
    for _ in range(interval):
        x = random.random()
        y = random.random()

        d = x * x + y * y

        if d <= 1:
            circle_points +=1
        
        square_points += 1

    return round (4 * (circle_points / square_points), 3)


print(estimate_pi(10000))

print ('***************** Estimating Pi ********************************')

'''
    You run an e-commerce website and want to record the last N order ids in a log. Implement a data 
    structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

'''
class MyLogClass(object):   

    def __init__(self):
        self._log = []
    
    def record(self, order_id):
        self._log.append(order_id)
    
    def get_last(self, i):
        return self._log[:i]
    
'''
my_log = {}
def record(order_id):
    my_log.update({order_id: order_id})

def get_last(i):
    return my_log[i]

def record_file(order_id):
    with open('my_log.txt', 'a') as log:
        log.write( str(order_id) + ':' + str(order_id) + '\n')
         

def get_last_file(i):
    with open('my_log.txt', 'r') as log:
        result = []
        for _ in range(i):
            result.append(log.readline())
        
        return result

record_file(1)
record_file(2)
record_file(3)

print(get_last_file(2))
'''
my_log = MyLogClass()
my_log.record(1)
my_log.record(3)
my_log.record(4)

print(my_log.get_last(2))

print ('***************** record the last N order ids in a log ********************************')

'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.
'''
def intersecting_node(list1=[], list2=[]):

    result = [v for v in list1 if v in list2]
    if result:
        return result[0]
    
    return []

class MyNodeLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class MyLinkedList(object):

    def __init__(self):       
        self.head = None
        self.tail = None
    
    def add(self, node):
        if not self.head:
            self.head = node
            self.tail = node            
        else:
            self.tail.next = node
            self.tail = node            
    
    def intersecting_node(self, other_list):
        temp_head = self.head

        while temp_head.next:
            result = other_list.find_node(other_list.head, temp_head.value)

            if result:
                return result
            else:
                temp_head = temp_head.next
        
        return None

    def find_node(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        if not node.next:
            return None
        
        return self.find_node(node.next, value)
 
#print (intersecting_node([3, 7, 8, 10], [99, 1, 8, 10]))

node1, node2, node3, node4 = MyNodeLinkedList(3), MyNodeLinkedList(7), MyNodeLinkedList(8), MyNodeLinkedList(10)

my_linked_list = MyLinkedList()
my_linked_list.add(node1)
my_linked_list.add(node2)
my_linked_list.add(node3)
my_linked_list.add(node4)

my_linked_list2 = MyLinkedList()
my_linked_list2.add(MyNodeLinkedList(99))
my_linked_list2.add(MyNodeLinkedList(1))
my_linked_list2.add(MyNodeLinkedList(8))
my_linked_list2.add(MyNodeLinkedList(10))

print (my_linked_list.intersecting_node(my_linked_list2))

print ('***************** linked list  ---  intersecting node ********************************')

'''
    Given a smaller strings and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation.
    s: abbc
    b: cbabadcbbabbcbabaabccbabc
'''

def find_permutations(s, b):
    pass


print (find_permutations('abbc', 'cbabadcbbabbcbabaabccbabc'))

print ('***************** String  ---  find permutations ********************************')