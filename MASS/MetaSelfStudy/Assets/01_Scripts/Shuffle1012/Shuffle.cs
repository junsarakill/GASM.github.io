using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shuffle : MonoBehaviour
{
    //int 변수 100개를 담을 수 있는 배열
    public int[] intList;

    //담을 변수 개수
    [Range(1,100)][SerializeField] int varAmount;

    void Start() {
        //AddRandomInt2List(out intList);
        //인덱스 대로 int 넣기
        intList = new int[varAmount];
        for(int i = 0; i < intList.Length; i ++)
        {
            intList[i] = i;
        }
    }

    //지정된 개수만큼 배열에 랜덤 int 채우기
    void AddRandomInt2List(out int[] intList)
    {
        //배열 선언
        intList = new int[varAmount];
        //랜덤 int를 배열 원소에 넣기
        for(int i = 0; i < intList.Length; i ++)
        {
            intList[i] = Random.Range(0, 9999);
        }
    }

    //셔플 함수
    void ListShuffle(int[] list)
    {   
        //배열 받아서 그 안의 원소의 순서를 랜덤으로 섞기
        
    }
}
