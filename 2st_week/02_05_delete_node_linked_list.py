class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value) # 삽입할 노드 생성
        # index가 0일 때는 링크드 리스트의 헤드를 삽일할 노드로 바꿔줘야 한다.
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self.get_node(index - 1) # 삽입할 노드 앞에 위치할 노드 찾기
        next_node = prev_node.next # 삽입할 노드 뒤에 위치할 노드 찾기
        prev_node.next = new_node # 이전 노드와 삽입할 노드 연결하기
        new_node.next = next_node # 삽입할 노드와 다음 노드 연결하기

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index) # 삭제할 노드
        prev_node.next = index_node.next # 삭제할 노드의 이전 노드와 삭제할 노드의 다음 노드랑 연결해주면 된다.

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()
