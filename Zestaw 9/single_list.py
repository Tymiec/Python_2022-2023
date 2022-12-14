# Do klasy SingleList dodać nowe metody.

    # def remove_tail(self): pass   # klasy O(n)
    #     # Zwraca cały węzeł, skraca listę.
    #     # Dla pustej listy rzuca wyjątek ValueError.

    # def join(self, other): pass   # klasy O(1)
    #     # Węzły z listy other są przepinane do listy self na jej koniec.
    #     # Po zakończeniu operacji lista other ma być pusta.

    # def clear(self): pass   # czyszczenie listy

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
        
class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0

        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:   self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("Lista jest pusta!")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1

        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Lista jest pusta!")
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return node

        while node.next != self.tail:
            node = node.next

        remove = self.tail
        self.tail = node

        return remove

    def join(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail

            self.length = other.length
        elif not other.is_empty():
            self.tail.next = other.head
            self.tail = other.tail

            self.length += other.length

        other.clear()

    def clear(self):
        self.tail = None
        self.head = None
        self.length = 0