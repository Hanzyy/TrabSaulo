# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Basic example of an adapter class to provide a stack interface to Python's list."""

# -*- coding: utf-8 -*-

# from ..exceptions import Empty
# import from exceptions

class Empty(Exception):
    def __init__(self, valor):
      self.valor = valor

    def __str__(self):
      return repr(self.valor)

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      print('pilha vazia')
      return None
    else:
      return self._data[-1]

  def pop(self):
    if self.is_empty():
      print('pilha vazia')
      return None
    else:
      return self._data.pop()

  def printStack(self):
    copia = ArrayStack() # instaciou pilha auxiliar
    print('[', end="")
    while(not self.is_empty()): # enquanto a pilha s nao ficar vazia
        print(self.top(), end=" ") # exibe o elemento do topo da pilha
        copia.push(self.pop()) # adicionar o elem do topo na pilha auxiliar e desempilhar
    while(not copia.is_empty()):
        self.push(copia.pop())
    copia = None
    print(']\n')

if __name__ == '__main__':






    S = ArrayStack()                 # contents: [ ]
    S.printStack()
    print(S.top())
    S.push(5)                        # contents: [5]
    S.printStack()
    S.push(3)                        # contents: [5, 3]
    S.printStack()
    print(len(S))                    # contents: [5, 3];    outputs 2
    print(S.pop())                   # contents: [5];       outputs 3
    S.printStack()
    print(S.is_empty())              # contents: [5];       outputs False
    print(S.pop())                   # contents: [ ];       outputs 5
    S.printStack()
    print(S.pop())  # contents: [ ];       outputs 5
    S.printStack()
    print(S.is_empty())              # contents: [ ];       outputs True
    S.push(7)                        # contents: [7]
    S.printStack()
    S.push(9)                        # contents: [7, 9]
    S.printStack()
    print(S.top())                   # contents: [7, 9];    outputs 9
    S.printStack()
    S.push(4)                        # contents: [7, 9, 4]
    S.printStack()
    print(len(S))                    # contents: [7, 9, 4]; outputs 3
    print(S.pop())                   # contents: [7, 9];    outputs 4
    S.push(6)                        # contents: [7, 9, 6]
    S.printStack()
    S.push(8)                        # contents: [7, 9, 6, 8]
    S.printStack()
    print(S.pop())                   # contents: [7, 9, 6]; outputs 8
    S.printStack()
