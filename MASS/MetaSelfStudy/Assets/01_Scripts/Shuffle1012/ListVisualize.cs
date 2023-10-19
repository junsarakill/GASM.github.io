using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

//리스트를 시각화해서 보여주기
public class ListVisualize : MonoBehaviour
{
    //리스트
    public int[] myList;
    //원소 객체 프리팹
    [SerializeField] GameObject elementUIF;

    private void Awake() {
        //자신의 원소 객체 리스트에 넣기
        
    }

    private void Start() {
        VisualizeList(myList);
    }

    //받은 리스트를 시각화
    void VisualizeList(int[] intList)
    {
        //우선 자기 자식을 전부 제거
        foreach(Transform child in transform)
        {
            Destroy(child.gameObject);
        }
        //intList의 각 원소들을 차례대로 생성후 text 변경
        //for(int i = 0; i < intList.Count; i++)
        //{
        //    GameObject child = Instantiate(elementUIF, transform);
        //    child.GetComponent<Element>().text.text = $"{intList[i]}";
        //}
        foreach(int num in intList)
        {
            GameObject child = Instantiate(elementUIF, transform);
            child.GetComponent<Element>().text.text = $"{num}";
        }
    }

    
}
