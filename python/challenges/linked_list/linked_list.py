class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):

        """
        takes in a value and insert this value with a refernce to the old head node abd push this value
        to be the new head of linked list
        """
        # create new node
        self.head = Node(value, self.head)
        return self.head

    def __iter__(self):
        """Tell Python that this class is iterable"""
        return self

    # def includes(self,value):

    def includes(self, value):
        """
        returns a bollean if the nodes exiest in the linked list
         and false if not
        """

        #   Current <-- Head
        current = self.head
        # WHILE Current is not NULL
        while current != None:
            #   IF Current.Value is equal to value
            if current.data == value:
                #     return TRUE
                return True
            #   Current <-- Current.Next
            else:
                current = current.next

        return False

    def __str__(self):
        """
          to string
        Arguments: none
        Returns: a string representing all the values in the Linked List,
         formatted as:
        "{ a } -> { b } -> { c } -> NULL"

        """
        string = ""
        current = self.head
        # WHILE Current is not NULL
        while current != None:
            #   IF Current.Value is equal to value
            value = current.data
            if current.next is None:
                string += "{" + f" {value} " + "}" + " -> NULL"
                break

            else:
                string += "{" + f" {value} " + "} -> "
                current = current.next
        #   Current <-- Current.Next
        #     return TRUE
        return string

    def append(self, value):
        """
        this function will look for the node that has node.next as none which
        will represnt the the last node then it will append the value(node)
        and it will give the new created node to that node .next
        """
        current = self.head
        while current:
            #   IF Current.next is equal to none that means this is the last node
            if current.next == None:

                current.next = Node(value)
                break
            current = current.next

    #   Current <-- Current.Next

    def append_multi(self, list):
        """
        takes in s list of nodes and add them to the end of the
        linked list
        """
        for item in list:
            self.append(item)
        return "ll"

    def insertBefore(self, targetValue, value):
        '''
        takes in a node and add it befor the requierd node
        
        '''
        # create new node
        newNode = Node(value)
        # find target node to insert
        node = self.head
        if node != None:
            # search nodes
            while node:
                if node.next == None:
                    break
                if node.next.data == targetValue:
                    newNode.next = node.next
                    node.next = newNode
                    break
                else:
                    node = node.next

    def insert_after(self, value, new_value):
        '''
        this will insert thr new_value after the node (value) in the 
        linked list 
        '''
        current = self.head

        while current is not None:
            if current.data == value:
                newNode = Node(new_value, current.next)
                current.next = newNode
                break
            current = current.next

    @classmethod
    def zipLists(cls, list1, list2):
        LinkedList.reverse(list1)
        LinkedList.reverse(list2)
        zip_ll = LinkedList()
        current = list1.head
        current2 = list2.head
        while current:
            zip_ll.insert(current.data)
            zip_ll.insert_after(current.data, current2.data)
            #  zip_ll.insertBefore(i.next,)
            current = current.next
            current2 = current2.next

        return zip_ll
    @classmethod   
    # Function to reverse the linked list
    def reverse(self,list):
        '''
        this method will reverse the order of the nodes inside the list 

         '''
        prev = None
        current = list.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        list.head = prev
        return list


    def length(self):
        '''
        this function returns the length of 
        the linked list 
        '''
        current = self.head 
        count = 0 
        while (current):
            count += 1
            current = current.next
        return count

    def kth_from_end(self,k):
        '''
         revrse the linked list 
         creat a counter if the counter value =k then return 
         node.data at that number
        '''
        if k > self.length():
           return 'the number you entered is longer than the list'
        if k < 0:
            k=abs(k)-1
            list=self
        else:    
            list=LinkedList.reverse(self)
        current=list.head
        count=0
        while current:
            if k==count:
                data=current.data
                break
            count+=1
            current=current.next
        print(str(self))
        return data


## testing ##

ll = LinkedList()
ll.insert(2)
# ll.insert(8)
# ll.insert(3)
# ll.insert(1)
# print(LinkedList.reverse(ll))
# ll2 = LinkedList()
# ll2.insert(4)
# ll2.insert(9)
# ll2.insert(5)
# print(str(ll))
# print(str(ll2))
# print(LinkedList.zipLists(ll, ll2))
print(ll.kth_from_end(0))

# ll.insert(3)
# #  # ll.insert(1)
# #  # ll.append(5)
# # ll.insert(5)
# # ll.insert(4)
# # ll.append_multi([5,3,3])
# ll.insert_after(1,22)
# #  # ll.append_multi([5,3,2])
# print(str(ll))

# print(str(ll))


# print(str(ll2))
