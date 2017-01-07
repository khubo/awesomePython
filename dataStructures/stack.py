#!/usr/bin/env python

class Stack:
    """ simple stack implementation using default list """

    def __init__(self, list=None):
        if list == None : list = []
        self.list = list

    def push(self, elem):
        self.list.append(elem)

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty !')
        else:
            return self.list.pop()

    def empty(self):
        if not len(self.list):
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            return self.list[len(self.list) - 1]

    def size(self):
        if len(self.list):
            return len(self.list)
        else:
            return 0
             
    def show_stack(self):
        print self.list


