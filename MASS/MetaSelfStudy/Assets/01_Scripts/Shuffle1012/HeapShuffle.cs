using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HeapShuffle : MonoBehaviour
{
    //힙 정렬
    //부모 인덱스 i 일때 자식은 왼쪽 ix2 , 오른쪽 ix2 + 1
    //자식 인덱스 i 일때 부모는 i/2
    //인덱스 찾기 편의를 위해 [0]은 비우기
    [SerializeField]int[] heap;

    [Range(0,100)]public int varAmount;
    private void Start() {
        heap = new int[varAmount];
    }

    private void Update() {
        if(Input.GetKeyDown(KeyCode.Alpha1))
        {
            print(heap[0]);
        }
    }
}

public class Heap
{
    int[] heap;
}
