# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:51:25 2019

@author: USER
"""

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertLeft(self, val):
        if self.left == None:
            self.left = Node(val)
        else:
            self.left.insertLeft(val)
            
    def insertRight(self, val):
        if self.right == None:
            self.right = Node(val)
        else:
            self.right.insertRight(val)
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

T = Node(10)
T.insertLeft(8)
T.insertRight(2)

T.PrintTree()
