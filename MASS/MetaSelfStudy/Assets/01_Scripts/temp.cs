using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class temp : MonoBehaviour
{
    temp()
    {
        a = 2;
    }
    public readonly int a;
    public const int c = 33;
    //public const int d;
    // Start is called before the first frame update
    void Start()
    {
        //a = 2;
        ////int[] p = {99,49,29};
        ////int [] q = {2,4,66};
        
        ////asd(p,q);
        //int b = a+12;
        //print(b);
        print(a);
        //a = 23;
        //a += 2;
        //c = 22;
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void asd(int[] progresses, int[] speeds)
    {
        Queue<int> pq = new Queue<int>();
//         결과 리스트
        List<int> result = new List<int>();
        
        
        for(int i = 0; i < progresses.Length; i++)
        {
            pq.Enqueue(i);
        }
//         큐가 남아있으면 진행
        while(pq.Count > 0)
        {
//         작업이 100인지 확인
            if(progresses[pq.Peek()] >= 100)
            {
//                 100이 아닌 작업이 나올때까지 pop 및 카운트
                int cnt = 0;
                while(pq.Count > 0 && progresses[pq.Peek()] < 100)
                {
                    pq.Dequeue();
                    cnt++;
                }
//                 카운트를 결과 리스트에 추가
                result.Add(cnt);
            }
//             아닐 경우 스피드 만큼 증가
            else
            {
                foreach(int index in pq)
                {
                    progresses[index] += speeds[index];
                }
            }
        }
    }
}
