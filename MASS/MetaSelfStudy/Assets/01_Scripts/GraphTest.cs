using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//그래프를 표현할 노드
public class GraphNode
{
    //자신의 데이터
    public int data;
    //자신과 연결된 노드 리스트
    public List<GraphNode> connNodeList = new List<GraphNode>();

    public GraphNode(int data)
    {
        this.data = data;
    }
}


public class GraphTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        GraphNode a1 = new GraphNode(1);
        GraphNode a2 = new GraphNode(2);
        
        a1.connNodeList.Add(a2);

        print(a1.connNodeList[0].connNodeList[0].connNodeList[0].connNodeList);

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
