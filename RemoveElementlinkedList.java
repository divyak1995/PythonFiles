class Main {
  Node head;
  static class Node {
    int value;
    Node next;
    public Node(int v) {
      value=v;
      next=null; 
    }
  }

  public void traversal() {
    Node n=head;
    while(n !=null) {
      System.out.print(n.value+" ");
      n=n.next;
    }
  }

  //insert a node into the linkedlist
  public void insert(Node element) {
    Node n=head;
    while(n!=null && n.next!=null) {
      n=n.next;
    }
    n.next = element;

  }

  //remove the last node from linkedlist
  public void removeLastNode() {
    Node n=head;
    while(n!=null && n.next !=null && n.next.next!=null) {
      n=n.next;
    }
    n.next=null;
  }

  //remove a specified node from the linkedlist
  public void removeNode(Node element) {
    if(head !=null && head.value==element.value) {
      Node p=head;
      head=head.next;
      p.next=null;
    }
    Node n=head.next;
    Node prev=head;
    while(n!=null) {
      if(n.value == element.value) {
        prev.next=n.next;
        n.next=null;
      }
      prev=n;
      n=n.next;
    }
  }

  public void reverseLinkedList() {
    Node prev=null;
    Node current = head;
    while(current != null) {
      Node nextNode=current.next;
      current.next=prev;
      prev=current;
      current=nextNode;
    }
    head=prev;
  }


  public static void main(String[] args) {
    Main llist= new Main();
    llist.head = new Node(1);
    Node second=new Node(2);
    Node third=new Node(3);
    llist.head.next=second;
    second.next=third;
    llist.traversal();
    Node element=new Node(4);
    llist.insert(element);
    Node element2=new Node(5);
    llist.insert(element2);
    System.out.println();
    llist.traversal();
    llist.removeLastNode();
    System.out.println();
    llist.traversal();
    llist.removeNode(second);
    System.out.println();
    llist.traversal();
    llist.reverseLinkedList();
    System.out.println();
    llist.traversal();

  }

}
