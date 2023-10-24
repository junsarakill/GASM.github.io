using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Node<T>
{
    public T data;
    public Node<T> next;

    public Node(T data)
    {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList<T>
{
    public Node<T> head;

    public void Add(T newData)
    {
        if(head == null)
        {
            head = new Node<T>(newData);
        }
        else
        {
            Node<T> temp = head;
            while(temp.next != null)
            {
                temp = temp.next;
            }
            temp.next = new Node<T>(newData);
        }
    }

    public void Remove(T rData)
    {
        Node<T> temp = head;
        Node<T> prev = temp;
        var tc = Comparer<T>.Default;
        
        //둘 다 같은지 비교하는 기능
        //while(!temp.data.Equals(rData))
        while(tc.Compare(temp.data, rData) != 0)
        {
            prev = temp;
            temp = temp.next;
        }

        if(temp == head)
            head = temp.next;
        else
            prev.next = temp.next;
    }

    public void Print()
    {
        Node<T> temp = head;
        string log = "";

        while(temp != null)
        {
            log += log == "" ? temp.data : $", {temp.data}";

            temp = temp.next;
        }
        Debug.Log(log);
    }
}

public class LinkedListManager : MonoBehaviour
{
    public LinkedList<int> asd = new LinkedList<int>();
    // Start is called before the first frame update
    void Start()
    {
        asd.Add(10);
        asd.Add(20);
        asd.Add(300);
        asd.Print();
        asd.Remove(10);
        asd.Print();

    }

    // Update is called once per frame
    void Update()
    {

    }
}
